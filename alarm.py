import sqlite3
import time
import webbrowser
from playsound import playsound

class Alarm:
    conn = None
    cursor = None
    def __init__(self):
        self.conn = sqlite3.connect('alarm.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        
    def submit(self, name, time, text):
        self.cursor.execute("INSERT INTO Alarms (name, time, link) VALUES (?, ?, ?)", [str(name), str(time), str(text)])
        self.conn.commit()
    
    def list_all(self):
        return self.cursor.execute("SELECT * FROM Alarms").fetchall()

    def close(self): 
        self.conn.close()
    
    def poll(self):
        while True:
            current_time = time.strftime("%H:%M", time.localtime())
            classroom = self.cursor.execute("SELECT * FROM Alarms WHERE time=?", [current_time]).fetchone()
            if classroom is not None:
                webbrowser.open_new(classroom[2])
                i = 0
                while i < 30:
                    playsound("BEEPDOWN.wav")
                    i+=1
            time.sleep(60)
        