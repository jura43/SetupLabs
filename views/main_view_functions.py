from PyQt6.QtWidgets import QFileDialog
from accsetupparse import McLaren720S
import json

def switchStackedWidget(widget, switchTo):
    """
    Function for switching window in stacked widget
    """

    widget.setCurrentWidget(switchTo)


def openFileOpenWindow(self, widget, switchTo):
    """
    Function provides all functionaly needed for loading and view setup
    It return setup object
    """
    fname = QFileDialog.getOpenFileName(self, "Select setup file", "", "ACC setup file (*.json)")

    s = open(fname[0]) 
    data = json.load(s)
    s.close()
    switchStackedWidget(widget, switchTo)

    

    return McLaren720S(data)