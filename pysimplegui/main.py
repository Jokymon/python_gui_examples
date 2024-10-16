import PySimpleGUI as sg


if __name__ == "__main__":
    sg.set_options(font=('Arial', 14))
    layout = [  [sg.Text("Lass dich begrüssen")],
                [sg.Text("Wie ist dein Name?"), sg.InputText(size=15, key='name')],
                [sg.Button('Begrüsse', expand_x=True)],
                [sg.Text("", key='greeting_output', expand_x=True)] ]
    
    window = sg.Window('PySimpleGUI Beispiel GUI', layout)
    
    while True:
        event, values = window.read()
    
        if event == sg.WIN_CLOSED:
            break

        if event == 'Begrüsse':
            name = values['name']
            window['greeting_output'].update(f"Hallo {name}")
    
    window.close()
