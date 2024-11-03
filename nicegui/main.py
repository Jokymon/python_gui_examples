from nicegui import ui


class Model:
    def __init__(self):
        self.name = ""
        self.greeting = ""

    def set_greeting(self, new_greeting):
        self.greeting = new_greeting


if __name__ in {"__main__", "__mp_main__"}:
    model = Model()

    ui.page_title("NiceGUI GUI Beispiel")
    ui.label('Lass dich begrüssen')

    with ui.row(align_items="baseline"):
        ui.label('Wie ist dein Name?')
        ui.input().bind_value(model, "name")

    ui.button('Begrüsse',
              on_click=lambda: model.set_greeting(f"Hallo {model.name}"))
    greeting_output = ui.label().bind_text_from(model, "greeting")

    ui.run()
