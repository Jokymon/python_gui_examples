import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PyQt5 Widgets Beispiel GUI")

        gridlayout = QGridLayout()

        label = QLabel(self, text="Lass dich begrüssen")
        gridlayout.addWidget(label, 0, 0)
        label = QLabel(self, text="Wie ist dein Name?")
        gridlayout.addWidget(label, 1, 0)

        self.name_widget = QLineEdit(self)
        gridlayout.addWidget(self.name_widget, 1, 1)

        self.greeting_button = QPushButton(self, text="Begrüsse")
        self.greeting_button.clicked.connect(self.greet_user)
        gridlayout.addWidget(self.greeting_button, 2, 0, 1, 2)

        self.greeting_output = QLabel(self)
        gridlayout.addWidget(self.greeting_output, 3, 0, 1, 2)

        self.setLayout(gridlayout)

    def greet_user(self):
        user_name = self.name_widget.text()
        self.greeting_output.setText(f"Hello {user_name}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("* {font-size: 14pt;}")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
