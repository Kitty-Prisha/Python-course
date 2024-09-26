def greet(name,message="Hi" ):
    return f"{message}{name} how are you "
print(greet("Prisha"))
#Positional arguements
def total(bill,percentage):
    total=bill+(1+0.001*percentage)
    total=round(total,2)
    print(total)
total(2000,20)


