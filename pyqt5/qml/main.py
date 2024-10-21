import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtGui import QFont
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication


class MyApplication(QObject):
    greetingChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._greeting = ""

    # Diese Methode kann aus QML aufgerufen werden, nachdem
    # wir eine Instanz von MyApplication erzeugt haben. Mit
    # dem Decorator @pyqtSlot müssen wir Qt gegenüber angeben,
    # welchen Datentyp der Parameter `name` von greet_user()
    # haben soll. Wir verwenden hier Zeichenketten, also `str`.
    @pyqtSlot(str)
    def greet_user(self, name):
        self._greeting = f"Hallo {name}"
        self.greetingChanged.emit()

    # Die Eigenschaft (Engl. Property) `greeting` ist
    # ebenfalls aus QML abrufbar. Damit QML weiss, wann es
    # das GUI neu zeichnen soll, müssen wir QML auch
    # informieren, wann dieses Property seinen Wert geändert
    # hat. Dies geschieht mit dem "Signal" `greetingChanged`.
    @pyqtProperty(str, notify=greetingChanged)
    def greeting(self):
        return self._greeting


if __name__ == '__main__':
    app = QApplication(sys.argv)
    default_font = QFont("Arial", 14)
    app.setFont(default_font)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)

    # Hier erzeugen wir die Instanz von MyApplication, sodass
    # diese dann ihre Funktionalität in QML anbieten kann. Der
    # Zugriff erfolgt über den Property-Namen "myapp".
    myapp = MyApplication()
    context = engine.rootContext()
    context.setContextProperty("myapp", myapp)

    engine.load('main.qml')

    sys.exit(app.exec())
