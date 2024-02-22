from obj.room import Room

from visualising import Initialise

# Debugging Variables
VisualiseRoom = True
Debug = False


# Stuff
MinAkku = 15#%
MinDreck = 85#%


# Liste die alle Räume beinhaltet : mehrdimensionale Liste 
RoomListe = []

# Turtle
Smol_turtle = None
if VisualiseRoom == True:
    Smol_turtle = Initialise()

# Funktion um einen Raum aus der Liste zu bekommen abhängig von den Koordinaten
def getRoom(RoomList, X,Y):
    for _i in RoomList:
        for _j in _i:
            if _j.getkuerzel() == str(X)+";"+str(Y):
                return _j
    return None


# CREATE ROOMS

# Directory von der config_room.txt -> Bidde ändern dankee :P
Config_Room = open(r"C:\Users\DarkA\OneDrive\VS\OOP\Staubsaugi NEW\config_room.txt", "r")

FullRoom = []

_Index = 0
for _Reihe in Config_Room:
    _Str_Reihe = str(_Reihe)
    _max_Reihe = len(_Str_Reihe)

    for _Int_Spalte in range(_max_Reihe):
        _Char = _Str_Reihe[_Int_Spalte]
        
        FullRoom.append([_Index, _Int_Spalte, _Char])
    
    _Index += 1

NewRoom = []
for _Element in FullRoom:
    if _Element[2] != "\n":
        CreatedRoom = Room(str(_Element[1])+";"+str(-(_Element[0])),"","")
        NewRoom.append(CreatedRoom)
        if _Element[2] == "#":
            CreatedRoom.settype("Wall")
        elif _Element[2] == ".":
            CreatedRoom.settype("Empty")
        elif _Element[2] == ",":
            CreatedRoom.setfloortype("Soft")
        elif _Element[2] == "c":
            CreatedRoom.settype("ChargingStation")
        elif _Element[2] == "x":
            CreatedRoom.settype("Blocked")
        
RoomListe.append(NewRoom)

if Debug == True:
    print(FullRoom)
    print(RoomListe)
    for _List in RoomListe:
        for _Obj in _List:
            print(_Obj.getkuerzel())

Config_Room.close()

possibleMoves = [(0, 1), (0, -1), (1, 0), (-1, 0)]