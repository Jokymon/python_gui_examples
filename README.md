# GUI library examples

This project offers beginners to Python programming a few very simple examples of how an
application could be built with the help of common GUI libraries. For more detailed
instructions and tutorials, please refer to respective project websites, blog articles and
Youtube videos. These examples are for inspiration only and by no means show the full
potential of the corresponding libraries.

Each subfolder represents a complete small project in one of the GUI technologies. You can 
use the complete contents of such a folder as a basis for your own projects.

## Details

 * Necessary libraries are stored in `requirements.txt`. These must first be installed using
   `pip install -r requirements.txt`.
 * Each project contains at least one `main.py`, which should be executed. Usually a
   `python main.py` is sufficient, but in certain technologies other steps may be necessary.
   These can be found in `README.md` of the subfolder.

## Features

When implementing the examples, care was taken to ensure that at least the following functions
are always implemented:

 * A name can be entered in a text field
 * When a button is clicked, the text is read from the name field and a greeting is generated,
   which is written to a label field
 * The title bar of the GUI is set
 * If necessary, the size of the window is set
 * If possible, the size of the window is set to the desired value.
