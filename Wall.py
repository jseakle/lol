from BoardObject import *

class Wall(BoardObject):

    def __init__(self, smap):
        BoardObject.__init__(self, smap)
        self.name = "Wall"
