class Room:
    
    '''
    Types
    
    Empty
    Wall
    Blocked
    ChargingStation

    FloorType

    Soft
    Hard
    '''

    # Kontruktor
    def __init__(self, kuerzel: str, type: str, floortype: str):
        self.setkuerzel(kuerzel)
        self.settype(type)
        self.setfloortype(floortype)


    # SETTER
    def setkuerzel(self, kuerzel):
        self.kuerzel = kuerzel
    
    def settype(self, type):
        self.type = type

    def setfloortype(self, floortype):
        self.floortype = floortype

    # GETTER
    def getkuerzel(self):
        return self.kuerzel
    
    def gettype(self):
        return self.type

    def getfloortype(self):
        return self.floortype
