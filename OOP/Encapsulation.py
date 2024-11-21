class Student:
    __schoolname="ABC school"
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def __dispaly(self):
        print("This is a private method" )
school=Student("Prisha",12) 
print(school.__display())
print(school.name)
print(school.age)      
        