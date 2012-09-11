import random
import json

from Cell import *
from Wall import *

class Map(object):

    def __init__(self, settings):
        self.realmap = []
        self.allobjectsever = []
        for i in xrange(settings[0]):
            self.realmap += [[]]
            for j in xrange(settings[1]):
                self.realmap[i] += [Cell()]

        for i in xrange(settings[2]):
            while True:
                x = random.randint(0, settings[0] - 1)
                y = random.randint(0, settings[1] - 1)

                if self.realmap[x][y].empty():
                    print x, y
                    self.realmap[x][y].place(Wall(self))
                    break
                

        self.genState((0,0))

    #Produce a static version of the map as is
    def genState(self, turn):
        for x in xrange(len(self.realmap)):
            for y in xrange(len(self.realmap[x])):
                for obj in self.realmap[x][y].contents:
                    obj.genState(turn, x, y)

    def getState(self, turn):
        return map(lambda x: x.getState(turn), self.allobjectsever)
        

