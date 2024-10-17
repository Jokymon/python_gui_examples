# GUI Bibliotheken-Beispiele

Dieses Projekt bietet Einsteigern in die Python-Programmierung ein paar ganz
einfache Beispiele, wie mit Hilfe geläufiger GUI-Bibliotheken eine Applikation
gebaut werden könnte. Für detailiertere Anleitungen und Tutorials sei auf
jeweiligen Projektwebseiten, Blogartikel und Youtube-Videos verwiesen. Diese
Beispiele dienen nur der Inspiration und zeigen keineswegs das vollständige
Potential der entsprechenden Bibliotheken.

Jeder Unterordner stellt ein komplettes kleines Projekt in einer
GUI-Technologie dar. Man kann also den kompletten Inhalt eines solchen Ordners
als Basis für eigene Projekte verwenden.

## Details

 * Nötige Bibliotheken werden in `requirements.txt` festgehalten. Diese müssen
   zuerst mit `pip install -r requirements.txt` installiert werden.
 * Jedes Projekt enthält mindestens ein `main.py`, welches ausgeführt werden
   soll. Üblicherweise reicht ein `python main.py`, in gewissen Technologien
   können aber andere Schritte notwendig sein. Diese sind im `README.md` des
   Unterordners zu finden.

## Features

Bei der Umsetzung der Beispiele wurde darauf geachtet, dass immer mindestens
folgende Funktionen umgesetzt sind:

 * In einem Text-feld kann ein Name eingegeben werden
 * Beim anclicken eines Buttons wird der Text aus dem
   Namensfeld gelesen und eine Begrüssung erzeugt, die
   in ein Label-Feld geschrieben wird
 * Die Titelzeile des GUIs wird gesetzt
 * Falls nötig wird die Grösse des Fensters festgesetzt
 * Falls möglich, wird ein Gridlayout oder etwas 
   ähnliches für die Anordnung der Elemente verwendet