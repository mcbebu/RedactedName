import PySimpleGUI as sg

layout = [
    [sg.Text("Parcel Density", size = (60, 1), justification="center")],
    [sg.Text("Choose a csv file to upload")],
    [sg.FileBrowse(key = "-BROWSER-")],
    [sg.Button("test", key = "-BUTTON-")]
]

window = sg.Window(title="Redacted Name Demo", layout= layout, margins=(100,50))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-BUTTON-":
        if values:
            print(5)
            print(len(values))
        

