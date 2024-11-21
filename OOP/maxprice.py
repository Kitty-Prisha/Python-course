class price:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price is ",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
max=price()
max.sell()                

        