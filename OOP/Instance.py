class fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __del__(self):
        print("Object has been deleted")    
    def intro(self):
        print("Fruit name is ",self.name,"Fruit color is ",self.color) 
apple=fruit("Apple","Red")
apple.intro()
del apple
        