# Modules
from time import sleep
import math

# Objects
from config import Smol_turtle

# Methods
from config import getRoom
from visualising import Visualise

from path_algorithm import aStar

# Variables
from config import Debug
from config import VisualiseRoom
from config import RoomListe

from config import MinAkku
from config import MinDreck

class Robot:

    # Konstruktor
    def __init__(self, name: str = "Experiment 3.0 V2", akku: object = None, cacheOpenRoom: list = [], cacheDrovenRoom: list = [], CurrentRoom: object = None, Speed: int = 1, drecktank: object = None, modi: str = "Saugen", modiSpeed: int = 1, CacheLastRoom: object = None):
        self.setname(name)
        self.setakku(akku)
        self.setcacheOpenRoom(cacheOpenRoom)
        self.setcacheDrovenRoom(cacheDrovenRoom)
        self.setcurrentRoom(CurrentRoom)
        self.setspeed(Speed)
        self.setdrecktank(drecktank)

        self.setmodi(modi)
        self.setmodiSpeed(modiSpeed)


    # Setter & Getter
    def setname(self, name):
        self._name = name

    def setakku(self, akku):
        self.akku = akku  

    def setdrecktank(self, drecktank):
        self.drecktank = drecktank

    def setmodi(self, modi):
        self.modi = modi

    def setmodiSpeed(self, modiSpeed):
        self.modiSpeed = modiSpeed

    def getname(self):
        return self._name
    
    def getakku(self):
        return self.akku
    
    def setcacheOpenRoom(self, cacheOpenRoom):
        self.cacheOpenRoom = cacheOpenRoom

    def setcacheDrovenRoom(self, cacheDrovenRoom):
        self.cacheDrovenRoom = cacheDrovenRoom

    def getcacheOpenRoom(self):
        return self.cacheOpenRoom
    
    def getcacheDrovenRoom(self):
        return self.cacheDrovenRoom
    
    def removecacheOpenRoom(self, room):
        self.cacheOpenRoom.remove(room)

    def addcacheDrovenRoom(self, room):
        self.cacheDrovenRoom.append(room)

    def setcurrentRoom(self, currentRoom):
        self.currentRoom = currentRoom

    def getcurrentRoom(self):
        return self.currentRoom

    def addcacheOpenRoom(self, room):
        self.cacheOpenRoom.append(room)

    def setspeed(self, speed):
        self.speed = speed

    def getspeed(self):
        return self.speed
    
    def getdrecktank(self):
        return self.drecktank
    
    def getmodi(self):
        return self.modi
    
    def getmodiSpeed(self):
        return self.modiSpeed

    def setCacheLastRoom(self, CacheLastRoom):
        self.CacheLastRoom = CacheLastRoom

    def getCacheLastRoom(self):
        return self.CacheLastRoom


    # Methods

    # Erhalte den am nähesten gelegenen Raum von einer gegeben Liste sowie einem gegebenen Raum wo es startet. SpecialRequirement ist optional und kann einen bestimmten Raumtypen verlangen.
    def GetNearestRoom(self, GivenList,ToRoom, SpecialRequirement = None):

        min_distance = 9999999
        RoomField_nearest = None

        for room in GivenList:
            distance = math.sqrt((int(room.getkuerzel().split(";")[0]) - int(ToRoom.getkuerzel().split(";")[0]))**2 + (int(room.getkuerzel().split(";")[1]) - int(ToRoom.getkuerzel().split(";")[1]))**2)
            if distance < min_distance:
                if SpecialRequirement == None or room.gettype() == SpecialRequirement:
                    min_distance = distance
                    RoomField_nearest = room

        return RoomField_nearest
    
    # Element für Pathfinding, quasi FindNextRoomToDriveToWhichIsCool Funktion nur Angepasst auf Pathfinding -> das Ziel soll erreicht werden
    def PathElement(self, RoomField_GoTo):

        RoomField_Current = self.getcurrentRoom()
        RoomField_Current_X = int(RoomField_Current.getkuerzel().split(";")[0])
        RoomField_Current_Y = int(RoomField_Current.getkuerzel().split(";")[1])

        RoomField_Left = getRoom(RoomListe, RoomField_Current_X-1, RoomField_Current_Y)
        RoomField_Right = getRoom(RoomListe, RoomField_Current_X+1, RoomField_Current_Y)
        RoomField_Top = getRoom(RoomListe, RoomField_Current_X, RoomField_Current_Y+1)
        RoomField_Bottom = getRoom(RoomListe, RoomField_Current_X, RoomField_Current_Y-1)
        # Genau die selbe Funktion wie FindNextRoomToDriveToWhichIsCool nur das es hier auf das Pathfinding angepasst ist
        # Aber auch nicht optimiert
        ChosenRoom = None
        if Debug == True:
            print("=====================================")
            if RoomField_Left:
                print("Room Left: "+RoomField_Left.getkuerzel()+" | "+RoomField_Left.gettype())
            if RoomField_Right:
                print("Room Right: "+RoomField_Right.getkuerzel()+" | "+RoomField_Right.gettype())
            if RoomField_Top:
                print("Room Top: "+RoomField_Top.getkuerzel()+" | "+RoomField_Top.gettype())
            if RoomField_Bottom:
                print("Room Bottom: "+RoomField_Bottom.getkuerzel()+" | "+RoomField_Bottom.gettype())

        if (RoomField_Left and (int(RoomField_Left.getkuerzel().split(";")[0]) >= int(RoomField_GoTo.getkuerzel().split(";")[0]))):
            if (RoomField_Left.gettype() != "Blocked" and RoomField_Left.gettype() != "Wall"):
                ChosenRoom = RoomField_Left
            else:
                #return [0,-1]
                pass
        if (RoomField_Top and (int(RoomField_Top.getkuerzel().split(";")[1]) <= int(RoomField_GoTo.getkuerzel().split(";")[1]))):
            if (RoomField_Top.gettype() != "Blocked" and RoomField_Top.gettype() != "Wall"):
                ChosenRoom = RoomField_Top
            else:
                #return [1,0]
                pass
        if (RoomField_Right and (int(RoomField_Right.getkuerzel().split(";")[0]) <= int(RoomField_GoTo.getkuerzel().split(";")[0]))):
            if (RoomField_Right.gettype() != "Blocked" and RoomField_Right.gettype() != "Wall"):
                ChosenRoom = RoomField_Right
            else:
                #return [0,1]
                pass
        if (RoomField_Bottom and (int(RoomField_Bottom.getkuerzel().split(";")[1]) >= int(RoomField_GoTo.getkuerzel().split(";")[1]))):
            if (RoomField_Bottom.gettype() != "Blocked" and RoomField_Bottom.gettype() != "Wall"):
                ChosenRoom = RoomField_Bottom
            else:
                #return [-1,0]
                pass

        if ChosenRoom != None:
            return ChosenRoom
        else:
            return None

    # Funktion die es ermöglicht selbstständig an Hindernissen vorbei zu fahren zu dem vorgegebenen Ziel
    def PathAndDriveToRoom(self,RoomField_GoTo):
        self.setmodi("Fahren")
        print("=====================================")
        print("Pathfinding")
        print("Modi switched to: "+self.getmodi())
        print("Driving Goal "+RoomField_GoTo.getkuerzel())

        while self.getcurrentRoom() != RoomField_GoTo:
            RoomField_Next = self.PathElement(RoomField_GoTo)

            if RoomField_Next is not None:
                self.setcurrentRoom(RoomField_Next)
                print("Driving to "+RoomField_Next.getkuerzel())
                if VisualiseRoom == True:
                    Visualise(Smol_turtle, int(RoomField_Next.getkuerzel().split(";")[0]),int(RoomField_Next.getkuerzel().split(";")[1]), RoomField_Next.gettype(), "Path")
                sleep(self.getspeed()*1*self.getmodiSpeed())
            elif RoomField_Next == "EW":
                print(RoomField_Next)
                print("=====================================")
                print("Err 05: Robi is stupid Robi is tired Robi is going to sleep")
                return False
            else:
                print("=====================================")
                print("Err 03: No Room Found")
                return True
            
        print("=====================================")
        print("Pathfinding Finished")
        return True


    # Funktion die "Systematisch" den Roboter den Raum abfahren lässt : Es kontrolliert wo der Roboter aktuell ist und welches Feld in seiner direkten Umgebung noch frei ist  
    def FindNextRoomToDriveToWhichIsCool(self):
        Dirty = self.getcacheOpenRoom()
        
        # Aktuelle Position + Raum des Roboters
        RoomField_Current = self.getcurrentRoom()
        RoomField_Current_X = int(RoomField_Current.getkuerzel().split(";")[0])
        RoomField_Current_Y = int(RoomField_Current.getkuerzel().split(";")[1])
        
        # Debug
        if Debug == True:
            print("=====================================")
            print("Current Room: "+RoomField_Current.getkuerzel())

        # Felder in der Umgebung
        RoomField_Left = getRoom(RoomListe, RoomField_Current_X-1, RoomField_Current_Y)
        RoomField_Right = getRoom(RoomListe, RoomField_Current_X+1, RoomField_Current_Y)
        RoomField_Top = getRoom(RoomListe, RoomField_Current_X, RoomField_Current_Y+1)
        RoomField_Bottom = getRoom(RoomListe, RoomField_Current_X, RoomField_Current_Y-1)

        # Debug
        ChosenRoom = None
        if Debug == True:
            print("=====================================")
            if RoomField_Left:
                print("Room Left: "+RoomField_Left.getkuerzel()+" | "+RoomField_Left.gettype())
            if RoomField_Right:
                print("Room Right: "+RoomField_Right.getkuerzel()+" | "+RoomField_Right.gettype())
            if RoomField_Top:
                print("Room Top: "+RoomField_Top.getkuerzel()+" | "+RoomField_Top.gettype())
            if RoomField_Bottom:
                print("Room Bottom: "+RoomField_Bottom.getkuerzel()+" | "+RoomField_Bottom.gettype())
        
        # Überprüfen ob der Raum existiert + ob er dreckig ist + ob er nicht blockiert ist + ob er keine Wand ist
        if (RoomField_Left and (RoomField_Left in Dirty) and RoomField_Left.gettype() != "Blocked" and RoomField_Left.gettype() != "Wall" ):
            ChosenRoom = RoomField_Left
        if (RoomField_Top and (RoomField_Top in Dirty) and RoomField_Top.gettype() != "Blocked" and RoomField_Top.gettype() != "Wall" ):
            ChosenRoom = RoomField_Top
        if (RoomField_Right and (RoomField_Right in Dirty)  and RoomField_Right.gettype() != "Blocked" and RoomField_Right.gettype() != "Wall" ):
            ChosenRoom = RoomField_Right
        if (RoomField_Bottom and (RoomField_Bottom in Dirty)  and RoomField_Bottom.gettype() != "Blocked" and RoomField_Bottom.gettype() != "Wall" ):
            ChosenRoom = RoomField_Bottom

        # Return falls der Raum existiert usw.
        if ChosenRoom != None:
            return ChosenRoom
        else:
            return None

    # Drecktank leeren
    def GoEmptyDirtTank(self):
        while self.getdrecktank().getcurrentcapacity() > 10:
            self.getdrecktank().setcapacity(self.getdrecktank().getcapacity()-10)
            print("Emptying... "+str(round(self.getdrecktank().getcurrentcapacity(), 2))+"%")
            sleep(0.01)

    # Akku laden
    def GoRecharge(self):
        while self.getakku().getcurrentcapacity() < 90:
            self.getakku().setcapacity(self.getakku().getcapacity()+10)
            print("Charging... "+str(round(self.getakku().getcurrentcapacity(), 2))+"%")
            sleep(0.01)

    # Zur Ladestation fahren per Pathfinding
    def GoToChargingStation(self, goal):
        self.setCacheLastRoom(self.getcurrentRoom())

        ChargingStation = None
        for _i in RoomListe:
            for _j in _i:
                if _j.gettype() == "ChargingStation":
                    ChargingStation = _j
                    break

        if ChargingStation != None:
            Success_P1 = self.PathAndDriveToRoom(ChargingStation)
            if Success_P1 == True:
                if goal == "Recharge":
                    self.GoRecharge()
                    return True
                elif goal == "Empty":
                    self.GoEmptyDirtTank()
                    return True
        else:
            return None


    # HauptFunktion - Start und Kontrollzentrum : Hier wird der komplette Raum abgefahren, 1: Systematisch, 2: Pathfinding
    def Start(self):
        print("Getting Settings")

        # Variables
        RobiSpeed = self.getspeed()

        # Unnötiger Bootup
        sleep(1)
        print("Initializing Driving Mode")
        sleep(1)
        for _ in range(4):
            print("Starting" + "." * _)
            sleep(0.25)
        print("Driving")
        
        # Driving Stuff

        # Liste aller dreckigen Räume
        DirtyList = self.getcacheOpenRoom()
        for _i in range(len(DirtyList)):
            # Raum der der Roboter als nächstes anfahren soll
            ChosenRoom = self.FindNextRoomToDriveToWhichIsCool()

            # Akku und Drecktank
            Akku = self.getakku()
            DirtTank = self.getdrecktank()

            # Wenn der Akku leer ist oder der Drecktank voll ist -> Zur Ladestation
            Success = None
            if Akku.getcurrentcapacity() <= MinAkku:
                Success = self.GoToChargingStation("Recharge")
            elif DirtTank.getcurrentcapacity() >= MinDreck:
                Success = self.GoToChargingStation("Empty")
            else:
                Success = True
            
            if Success == None:
                print("=====================================")
                print("Err 04: No Charging Station Found")
                break
            elif Success == True:
                #self.PathAndDriveToRoom(self.getCacheLastRoom())
                pass

            if ChosenRoom != None:
                # Raum gefunden -> Säuberungsprozess
                print("=====================================")
                print("Driving to "+ChosenRoom.getkuerzel())
                self.setcurrentRoom(ChosenRoom)

                # Je nach Bodenart wird gewischt oder gesaugt
                if ChosenRoom.getfloortype() == "Hard":
                    self.setmodi("Saugen")
                else:
                    self.setmodi("Wischen")

                if Debug == True:
                    print("Modi switched to: "+self.getmodi())

                print("Cleaning...")
                
                # Akku und Drecktank nach Raumsäubern angepasst
                Akku.setcapacity(Akku.getcapacity()-18)
                self.removecacheOpenRoom(ChosenRoom)
                self.addcacheDrovenRoom(ChosenRoom)
                sleep(RobiSpeed*0.5*self.getmodiSpeed())
                DirtTank.setcapacity(DirtTank.getcapacity()+19)
                print("Room Cleaned")
                print("Charge Left: "+str(round(Akku.getcurrentcapacity(), 2))+"%")
                print("Dirt in Tank: "+str(round(DirtTank.getcurrentcapacity(), 2))+"%")
                # Visualisierung
                if VisualiseRoom == True:
                    Visualise(Smol_turtle, int(ChosenRoom.getkuerzel().split(";")[0]),int(ChosenRoom.getkuerzel().split(";")[1]), ChosenRoom.gettype(), "Cleaned")
                sleep(RobiSpeed*0.5*self.getmodiSpeed())
            else:
                # Kein Raum gefunden -> Pathfinding Versuch
                print("=====================================")
                print("Err 01: No Room Found")
                Dirty = self.getcacheOpenRoom()
                # Der näheste Raum wird gesucht
                NearestRoom = self.GetNearestRoom(Dirty, self.getcurrentRoom(),"Empty")
                if NearestRoom == None:
                    # Kein freien Raum in der Nähe gefunden -> Abbruch
                    print("=====================================")
                    print("Err 02: No Nearest Room Found in given List")
                    break
                else:
                    # Freien Raum gefunden -> Pathfinding
                    print("Nearest room:" + str(NearestRoom.getkuerzel()))
                    Success_P2 = self.PathAndDriveToRoom(NearestRoom)
                    if Success_P2 == True:
                        # Doppelt ist immer gut
                        # Pathfinding erfolgreich -> Raum wird gesäubert
                        if NearestRoom.getfloortype() == "Hard":
                            self.setmodi("Saugen")
                        else:
                            self.setmodi("Wischen")

                        if Debug == True:
                            print("Modi switched to: "+self.getmodi())
                        print("Cleaning...")
                        Akku = self.getakku()
                        Akku.setcapacity(Akku.getcapacity()-6)
                        self.removecacheOpenRoom(NearestRoom)
                        self.addcacheDrovenRoom(NearestRoom)
                        sleep(RobiSpeed*0.5*self.getmodiSpeed())
                        DirtTank = self.getdrecktank()
                        DirtTank.setcapacity(DirtTank.getcapacity()+6)
                        print("Room Cleaned")
                        print("Charge Left: "+str(round(Akku.getcurrentcapacity(), 2))+"%")
                        print("Dirt in Tank: "+str(round(DirtTank.getcurrentcapacity(), 2))+"%")
                        if VisualiseRoom == True:
                            Visualise(Smol_turtle, int(NearestRoom.getkuerzel().split(";")[0]),int(NearestRoom.getkuerzel().split(";")[1]), NearestRoom.gettype(), "Cleaned")

        print("=====================================")
        print("Finished Cleaning")


    def Special(self):
        # A_Start Pathfinding
        # Gescheitertes Projekt
        grid = RoomListe
        start = grid[0][0]
        end = grid[0][12]

        path = aStar(start, end, grid)
        print(path)

'''
To-Do:

- Kaffee Pause

'''