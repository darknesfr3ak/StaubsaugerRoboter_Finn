class Akku:

    # Konstruktor
    def __init__(self, capacity, maxcapacity):
        self.setcapacity(capacity)
        self.setmaxcapacity(maxcapacity)


    # Setter & Getter
    def setcapacity(self, capacity):
        self.capacity = capacity

    def getcapacity(self):
        return self.capacity
    
    def setmaxcapacity(self, maxcapacity):
        self.maxcapacity = maxcapacity

    def getmaxcapacity(self):
        return self.maxcapacity
    
    def getcurrentcapacity(self):
        return ( self.getcapacity() / self.getmaxcapacity() ) * 100