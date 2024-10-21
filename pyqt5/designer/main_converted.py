import sys
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Das Feld `greet_button` ist Teil der Klasse `Ui_MainWindow`,
        # da wir im Designer dem Button den "objectName" auf den Wert
        # "greet_button" gesetzt haben.
        self.greet_button.clicked.connect(self.greet_user)

    def greet_user(self):
        # Genau gleich wie beim `greet_button`, haben wir auch die
        # "objectName" für `name_widget` und `greeting_output` im
        # Designer gesetzt.
        user_name = self.name_widget.text()
        self.greeting_output.setText(f"Hello {user_name}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("* {font-size: 14pt;}")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
