class BMW:
    def __init__(self,maxspeed,mileague):
        self.maxspeed=maxspeed
        self.mileague=mileague
    def write(self):
        print("The maxspeeed of BMW is ",self.maxspeed,"And the mileague is ",self.mileague)    
class Ferarri:
    def __init__(self,maxspeed,mileague):
        self.maxspeed=maxspeed
        self.mileague=mileague
    def write(self):
        print("The maxspeeed of Ferrari is ",self.maxspeed,"And the mileague is ",self.mileague)    
objBMW=BMW(190,61)
objferrari=Ferarri(217,488) 
for i in (objBMW,objferrari):
 i.write()       
                
        