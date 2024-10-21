import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 370
    height: 170
    title: "PyQt5 QML Beispiel GUI"

    GridLayout {
        anchors.fill: parent
        columns: 2

        Text {
            Layout.columnSpan: 2
            text: "Lass dich begrüssen"
        }

        Text {
            Layout.fillWidth: true

            text: "Wie ist dein Name?"
        }
        TextField {
            id: greet_input

            Layout.alignment: Qt.AlignLeft
            Layout.fillWidth: true
        }

        Button {
            Layout.alignment: Qt.AlignHCenter
            Layout.columnSpan: 2
            text: "Begrüsse"

            // Mit `onClicked` können wir ein Verhalten
            // definieren, dass beim Drücken dieses
            // Buttons ausgeführt werden soll. Wir wollen
            // hier den "slot" `greet_user` in `myapp`
            // aufrufen und dabei den aktuellen Wert des
            // `text`-Property vom `greet_input`-Feld übergeben.
            onClicked: myapp.greet_user(greet_input.text)
        }

        Text {
            id: output
            Layout.columnSpan: 2
            // Hier holen wir uns den aktuellen Wert des
            // Property `greeting` aus der Instanz `myapp`.
            // Diese Darstellung wird aktualisiert, sobald
            // sich der Wert des Properties verändert und
            // über das `notify`-Signal eine entsprechende
            // Benachrichtigung geschickt wurde.
            text: myapp.greeting
        }
    }
}