def planecost(city):
    if city=="Mumbai":
        return 6000
    elif city=="Delhi":
        return 7000
    elif city=="Kolkata":
        return 5500
def carcost(days):
    rentcost=int(input("Enter the rental cost"))
    if days>4:
        return 6700
    elif days<4:
        return 4000
def totalcost(city,days,spendingmoney):
    return carcost(days)+planecost(city)+spendingmoney
print(totalcost("Mumbai",6,7000))
print(totalcost("Delhi",7,8000))
print(totalcost("Kolkata",3,4000))
