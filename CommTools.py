# CommTools
# Class to facilitate passing messages back to morpho via txt file
# By: Sam Hocking

import os

class Comm():
    def __init__(self, filename):
        self.filename = filename
    def write(self, string):
        self.remove()
        with open(self.filename, 'w') as f:
            f.write(string)
    def remove(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)