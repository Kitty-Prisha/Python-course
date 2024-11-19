class bird:
    def __init__(self):
        print("The bird is ready")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__
        print("The Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
peg=penguin()
peg.whoisthis()
peg.swim()
peg.run()         
                    

        