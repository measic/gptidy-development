import ipywidgets as widgets
import json
import time
from threading import Thread
from traitlets import Int, Unicode, Tuple, CInt, Dict, validate, observe


class cyjsWidget(widgets.DOMWidget):
    
    _view_name = Unicode('CyjsView').tag(sync=True)
    _view_module = Unicode('cyjs').tag(sync=True)
    frameWidth = Int(400).tag(sync=True)
    frameHeight = Int(300).tag(sync=True)
    msgFromKernel = Unicode("{}").tag(sync=True)
    msgToKernel = Unicode("{}").tag(sync=True)
    status = "initial status message\n"
    selectedNodes = [];
    incomingMessageArrivedAndParsed = False;
    globalStatus = "blank"

