import PySimpleGUI as sg
import alarm
import threading

def class_view():
    alarm_instance= alarm.Alarm()
    class_list = alarm_instance.list_all()
    alarm_instance.close()
    layout = []

    for classroom in class_list:
        layout.append([sg.Text("Classname:"), sg.Text(classroom[0])])
        layout.append([sg.Text("Time:"), sg.Text(classroom[1])])
        layout.append([sg.Text("Link:"), sg.Text(classroom[2])])

    window = sg.Window("Classrooms", layout=layout)
    while True:
        event, values = window.read()
        if event  == sg.WIN_CLOSED:
            break
    window.close()

alarm_instance = alarm.Alarm()

def main_view():

    layout = [  
        [sg.Text('Class Name')],
        [sg.Input(key="Class")], 
        [sg.Text('Time')],
        [sg.Input(key="Time")],
        [sg.Text('Meet Link')],
        [sg.Input(key="Link")],
        [sg.Button("Submit"), sg.Button("View Classes")]
    ] 
    
    window = sg.Window('School Planner', layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break   

        if event == "Submit":
            alarm_instance.submit(values["Class"], values["Time"], values["Link"])
    
        if event == "View Classes":
            class_view()

    window.close()

if __name__ == "__main__":
    thread = threading.Thread(target=alarm_instance.poll, daemon=True)
    thread.start()
    main_view()