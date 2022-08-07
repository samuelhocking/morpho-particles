# datetimeTimingTools
# pass-through methods to access python datetime objects from another script
# By: Sam Hocking

from datetime import datetime
import os
from CommTools import Comm

class datetimeTimingTools():
    def __init__(self, format="%Y-%m-%d/%H:%M:%S.%f"):
        self.format = format
    def writeDT(self):
        now = datetime.now()
        string = now.strftime(self.format)
        Comm('comm.txt').write(string)
    def DTDiff(self, strStart, strEnd):
        dtStart = datetime.strptime(strStart, self.format)
        dtEnd = datetime.strptime(strEnd, self.format)
        seconds = (dtEnd - dtStart).total_seconds()
        Comm('comm.txt').write(str(seconds))