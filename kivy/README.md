Bauen von Android Apps ist aktuell nur unter Linux oder mit WSL unter
Windows möglich. Dazu befolgt man am besten die Anleitung unter
[Buildozer Installation](https://buildozer.readthedocs.io/en/latest/installation.html).

Wenn alle nötigen Dependencies gemäss Buildozer-Anleitung sowie eventuell
`python3.10-venv` oder eine neuere Version installiert sind, kann es mit
einem neuen virtual environment losgehen:

```bash
python3 -mvenv .venv
source .venv/bin/activate
```

Nun werden die Projekt-Dependencies und die Build-Depdencies (Buildozer und Cython)
in das Environment installiert

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Und schliesslich kann die Android-App gebaut werden mit dem folgenden simplen
Kommando. Es ist zu beachten, dass dies beim ersten Bauen bis zu 60 oder 90
Minuten dauern kann und bis zu 3-4GB an Festplattenspeicher benötigt, da
Buildozer erst noch die ganzen Android SDK/NDK Pakete herunter lädt und 
installiert.

```bash
buildozer android debug
```
