import PySimpleGUI as sg
from K_means import k_means_constrained 
from K_means import create_proximity_map

def run() :
    def make_first_layout():
        layout1 = [
            [sg.Text("Parcel Density", size = (60, 1), justification="center", font = "sans-serif, 25")],
            [sg.Text("Choose a csv file to upload", justification="center")],
            [sg.FileBrowse(key = "-BROWSER-")],
            [sg.Text("Minimum orders:")],
            [sg.Input(key = "-MIN_ORDERS-")],
            [sg.Text("Maximum orders:")],
            [sg.Input(key = "-MAX_ORDERS-")],
            [sg.Text("Number of drivers:")],
            [sg.Input(key = "-NUM_DRIVERS-")],
            [sg.Button("Get Proximity Clusters", key = "-PROX-")]
        ]
        return sg.Window("Redacted Name Demo", layout= layout1, margins=(100, 200), finalize=True)

    def make_second_layout():
        layout2 =  [
            [sg.Text("Parcel Density", size = (60, 1), justification="center")],
            [sg.Image("googlemaps.png", size = (500, 500))],
            [sg.Button("Back to Browse", key = "-REVERT-")]
        ]
        return sg.Window("Redacted Name Demo", layout= layout2, margins=(50, 50), finalize=True)

    window1, window2 = make_first_layout(), None

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-PROX-":
            print(values)
            if values["-BROWSER-"] and values["-MIN_ORDERS-"] and values["-MAX_ORDERS-"] and values["-NUM_DRIVERS-"]:
                data, clusters, labels, = k_means_constrained(values["-BROWSER-"], int(values["-MIN_ORDERS-"]), int(values["-MAX_ORDERS-"]), int(values["-NUM_DRIVERS-"]))
                create_proximity_map(data, labels)
                window2 = make_second_layout()
                window1.close()
        elif event == "-REVERT-":
            window1 = make_first_layout()
            window2.close()


    

