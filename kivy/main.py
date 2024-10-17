from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class GreetWindow(BoxLayout):
    def greet(self):
        # In self.ids sind alle Widgets verfügbar, die im .kv-File
        # mit `id: ` mit einer id versehen worden sind.
        name = self.ids.name_widget.text
        output_label = self.ids.greeting_output
        output_label.text = f"Hallo {name}"


class GreetApp(App):
    # Die Darstellung für die GreetApp ist in greet.kv beschrieben. Wenn
    # GreetApp z.B. in HelloApp umbenannt würde, müsste auch greet.kv in
    # hello.kv umbenannt werden.
    def build(self):
        self.title = "Kivy Beispiel GUI"
        Window.size = (400, 150)
        return GreetWindow()


if __name__ == '__main__':
    GreetApp().run()
