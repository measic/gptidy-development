import ipywidgets as widgets
import json
import time
from threading import Thread
from traitlets import Int, Unicode, Tuple, CInt, Dict, validate, observe


class newcyjsWidget(widgets.DOMWidget):
    
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

    #------------------------------------------------------------------------------
    class MyThread(Thread):
       owner = None
       def __init__(self, owner, group=None, target=None, name=None,
                    args=(), kwargs=None, *, daemon=None):
          Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
          self.owner = owner

       def run(self):
          maxLoops = 5
          counter = 0
          while((self.owner.incomingMessageArrivedAndParsed == False) and (counter < maxLoops)):
             counter += 1
             print("thread, no message yet, sleeping, loop %d" % counter)
             time.sleep(1.0)
          self.owner.status += "thread owner's selectedNodes: %s\n" % self.owner.selectedNodes;
          self.owner.status += "MyThread ending loop\n";

       def result(self):
          #while(not self.owner.incomingMessageArrivedAndParsed):
          #   time.sleep(0.1)
          return("imaap? %s" % self.owner.incomingMessageArrivedAndParsed)
            
    #------------------------------------------------------------------------------

    def testThread(self):
      for i in range(4):
         threadName = "Thread-%s" % (i + 1)
         mythread = self.MyThread(name=threadName, owner=self)
         mythread.start()
    
    def setSize(self, width, height):
      self.status += "setSize(%d, %d)\n" % (width, height)
      self.frameWidth = width
      self.frameHeight = height
        
    def fit(self, margin=50):
      self.status += "entering fit (%d)\n" % margin
      self.msgFromKernel = json.dumps({"cmd": "fit", "status": "request",
                                       "callback": "", "payload": margin});
    def getSelectedNodes(self):
      #self.selectedNodes = [];
      self.incomingMessageArrivedAndParsed = False;
      self.status += "entering getSelectedNodes\n";
      self.msgFromKernel = json.dumps({"cmd": "cleanSlate", "status": "request", "callback": "", "payload":""});
      self.msgFromKernel = json.dumps({"cmd": "getSelectedNodes", "status": "request",
                                       "callback": "", "payload": ""});
      
      observingThread = self.MyThread(name="getSelectedNodes-thread", owner=self)
      print("getSelectedNodes about to start observingThread")
      #observingThread.start()
      #observingThread.join()
      #while(self.incomingMessageArrivedAndParsed == False):
      #   time.sleep(0.5)
      observingThread.start()
      self.status += "getSelectedNodes, observingThread now started: %s\n" %  self.selectedNodes
      self.status += "getSelectedNodes, incomingMessageArrivedAndParsed? %s\n" % self.incomingMessageArrivedAndParsed
      return(observingThread.result())
        #return(self.status)
        
    def selectNodes(self, nodes):
      self.msgFromKernel = json.dumps({"cmd": "selectNodes", "status": "request",
                                       "callback": "", "payload": nodes});
       
    def clearSelection(self):
      self. msgFromKernel = json.dumps({"cmd": "clearSelection", "status": "request",
                                        "callback": "", "payload": ""});
        
    @observe('msgToKernel')
    def msg_arrived(self, change):
        self.status += "---- python - msg arrived\n"
        tmp = change['new']
        self.status += "len of tmp: %d\n" % len(tmp)
        self.status += "type of tmp: %s\n" % type(tmp)
        self.msgToKernel = tmp
        self.status += "%s\n" % tmp
        self.incomingMessageArrived = True
        self.dispatch(self.msgToKernel)
 
    def dispatch(self, msgRaw):
        self.msg = json.loads(msgRaw)
        self.status += "entering dispatch\n"
        self.status += "dispatch this msg: %s\n" % self.msg
        self.status += "msg.cmd: %s\n" % self.msg["cmd"]
        if self.msg["cmd"] == 'storeSelectedNodes':
            self.status += "storing selected nodes to self.selectedNodes %s\n" % msg["payload"]
            self.selectedNodes = msg["payload"]
        elif self.msg["cmd"] == 'clearCircles':
            self.circles = []
        else:
          print("unknown cmd: %s" % self.msg["cmd"])
        self.incomingMessageArrivedAndParsed = True
        
    def getResponse(self):
        return(self.msg["payload"])
    
