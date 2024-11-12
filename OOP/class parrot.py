class parrot:
    species="bird"
    def __init__(self,color,name):
        self.color=color
        self.name=name
blue=parrot("red","Blue") 
woo=parrot("Green","Woo") 
print(blue.species)
print(woo.species)
print(blue.name,blue.color)
print(woo.name,woo.color)        
        