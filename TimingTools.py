# datetimeTimingTools
# pass-through methods to access python datetime objects from another script
# By: Sam Hocking

from datetime import datetime
import os
from CommTools import Comm

class datetimeTimingTools():
    def __init__(self, filename="comm.txt", format="%Y_%m_%d_%R"):
        self.format = format
        self.filename = filename
    def writeDT(self):
        now = datetime.now()
        string = now.strftime(self.format)
        Comm(self.filename).write(string)
    def DTDiff(self, strStart, strEnd):
        dtStart = datetime.strptime(strStart, self.format)
        dtEnd = datetime.strptime(strEnd, self.format)
        seconds = (dtEnd - dtStart).total_seconds()
        Comm(self.filename).write(str(seconds))