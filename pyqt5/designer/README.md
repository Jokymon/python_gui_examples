## Einstieg

Dieses Vorgehen ist viel ausführlicher im 
[PyQt5 Tutorial](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
beschrieben.

## GUI designen

In `requirements.txt` wird zusätzlich ein Paket `PyQt5Designer`
installiert. Dieses Pakete enthält ein Programm, mit welchem
graphisch GUIs erstellt und bearbeitet werden können. Um das Programm
zu starten, muss man sich im entsprechenden Virtual Environment
befinden und dann folgendes im Terminal eingeben:

```
designer
```

Nun öffnet sich der Designer und es kann mit der Arbeit begonnen
werden. Fertig designte GUIs werden in einer Datei mit der Endung
`.ui` gespeichert. Um diese Dateien in Python zu verwenden, gibt
es zwei Möglichkeiten 1) Das `.ui`-File in eine Python-Datei
konvertieren und 2) Das `.ui`-File mit Python laden.

Die erste Variante erfordert einen zusätzlichen Schritt während
der Entwicklung des GUI, an den man immer denken muss, wenn man
weitere Änderungen mit dem Designer vornimmt. Der Vorteil ist aber,
dass sich die Auslieferung einer direkt ausführbaren Applikation
vereinfachen kann, da man es am Ende nur mit reinen Python-Dateien
zu tun hat. Zusätzlich ist diese Variante etwas performanter, da
nicht jedes Mal die `.ui`-Datei eingelesen werden muss.

### `.ui`-File konvertieren

Diese Variante ist in der Datei `main_converted.py` implementiert.

Der QtDesigner speichert den Aufbau des GUI in einem eigenen Format,
welches von Python nicht direkt verarbeitet werden kann. Es muss
zuerst noch in eine verarbeit-bare Form gebracht werden. Dafür ist
das Tool `pyuic5` zuständig. Nach jeder Änderung mit dem Designer,
muss die Python-Version des GUI wieder neu generiert werden.

Unter Windows:

```powershell
pyuic5.exe mainwindow.ui -o mainwindow.py
```

Unter MacOS und Linux:

```bash
pyuic5 mainwindow.ui -o mainwindow.py
```

### `.ui`-File mit Python laden

Diese Variante ist in der Datei `main_direct.py` implementiert.

In dieser Variante ist kein Konvertierungsschritt nötig, da das
`.ui`-File direkt von Python geladen wird. Der wesentliche
Unterschied in der Implementierung ist der zusätzliche import
von `uic` aus `PyQt5` sowie der Funktionsaufruf `uic.loadUi()`.
