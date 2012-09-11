class BoardObject(object):
    
    def __init__(self, smap):
        self.__hist = {}
        self.__map = smap
        self.__map.allobjectsever += [self]

    def genState(self, turn, x, y):
        
        self.__hist[turn] = {"x" : x, "y" : y}
        for attr in filter(lambda x: not x.startswith("_") and not hasattr(self.__getattribute__(x), "__call__"), dir(self)):
            self.__hist[turn][attr] = self.__getattribute__(attr)
        
    def getState(self, turn):
        try:
            return self.__hist[turn]
        except Exception:
            return None
