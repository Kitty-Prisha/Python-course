import os
shutdown=input("Do u want to shut down your computer?yes/no")
if shutdown=="no":
    exit()
else:
    os.system("shutdown/s/t 1")    
