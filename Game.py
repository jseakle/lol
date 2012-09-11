import pickle
import random

from Map import *

class Game(object):

    Ranked, Unranked = range(2)
    Blind, Draft, Random = range(3)

    phases = 3

    def __init__(self, sid, stype = Unranked, smode = Draft, spublic = False, mapsettings = (4, 4, 3) ):
        self.id = sid
        self.type = stype #ranked?
        self.mode = smode #draft?
        self.public = spublic

        self.players = []

        # Pending meta requests (rewind, draw, etc)
        self.requests = [];
        
        self.rosters = {}
        if self.mode == self.Draft:
            self.bans = {}
        
        self.map = Map(mapsettings)
        self.states = {}
        self.states[(0,0)] = self.map.getState((0,0))

        



        
        
        
        


        
