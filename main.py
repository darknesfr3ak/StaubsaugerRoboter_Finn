'''
WICHTIG

Unten Details!

+ Extra
    - A_Star Pathfinding (Gescheitert)
    - Roboter ist ein der Pre Alpha Version und besitzt neuste Technologie:
        = Kann Materie sowie sich selbst teleportieren
'''


# Modules
from obj.akku import Akku
from obj.robot import Robot
from obj.dirt import Dirt

# Objects 
## Objekte werden erstellt :P
Lithium_Ionen_Akku = Akku(1000,1000)

Drecktank = Dirt(0,1000)

Robi = Robot(name="Robi", akku=Lithium_Ionen_Akku, drecktank=Drecktank)



# Methods
from visualising import Visualise
from config import getRoom

# Variables
from config import RoomListe
from config import VisualiseRoom
from visualising import EndVisualising
from config import Smol_turtle
from config import Debug

# Den Robi seine Settings geben
Robi.setspeed(0.1) # - 1/10 der normalen Geschwindigkeit
Robi.setmodiSpeed(1)

# Den Robi in seinen Cache alle Räume hinzufügen (als Dreckig)
for _i in RoomListe:
    for _j in _i:
        if VisualiseRoom == True:
            Visualise(Smol_turtle, int(_j.getkuerzel().split(";")[0]),int(_j.getkuerzel().split(";")[1]), _j.gettype(),"",_j.getfloortype())

        if Debug == True:
            print(_j.getkuerzel())
            print(_j.getkuerzel().split(";")[0])
            print(_j.getkuerzel().split(";")[1])
        
        Robi.addcacheOpenRoom(_j)

        if _j.gettype() == "ChargingStation":
            # Den Robi sagen wo er sich gerade befindet
            Robi.setcurrentRoom(_j)


# Robi starten :D
Robi.Start()

# A_Star Pathfinding (Gescheitert)
#Robi.Special()

EndVisualising()

'''
WICHTIG

Pfad von config_room.txt in config.py Zeile 35 anpassen

Um den Raum zu verändern:
    config_room.txt
    x = Blockiert
    . = Harter Boden
    , = Weicher Boden
    # = Wand
    c = Ladestation

Gibt auch eine Config für Debug
'''
