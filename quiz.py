import random
class fruitquiz:
    def __init__(self):
        self.fruits= {'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}
    def quiz(self):
        while(True):
            fruit, color= random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_input=input()
            if(user_input.lower()==color):
                print("Correct answer")
            else:
                print("Wrong answer") 
            option=int(input("If you want to play again, enter 0, otherwise enter 1"))
            if (option):
                break
print("Welcome to fruit quiz")
fq= fruitquiz()
fq.quiz()



        