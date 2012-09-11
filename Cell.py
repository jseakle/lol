class Cell(object):
    
    def __init__(self):
        self.contents = []

    
    def place(self, obj):
        self.contents += [obj]

    def empty(self):
        return len(self.contents) == 0

    
