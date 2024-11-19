class vechile:
    def __init__(self,maxspeed,mileague,name):
        self.maxspeed=maxspeed
        self.mileague=mileague
        self.name=name
class Bus(vechile):
    pass
schoolbus=Bus(120,48,"XUV")
print(schoolbus.maxspeed,schoolbus.mileague,schoolbus.name)        
        