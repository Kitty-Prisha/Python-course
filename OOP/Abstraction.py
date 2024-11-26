from abc import ABC, abstractmethod
class abcclass(ABC):
    def Print(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("We are inside abc task")
taskobj=abcclass()
taskobj.task()
taskobj.print(19)


        
    