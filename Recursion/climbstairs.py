def ways(stairs):
    if stairs<0:
        return 0
    if stairs==1:
        return 1
    onestep=0
    twostep=0
    if (stairs>=2):
        twostep=ways(stairs-2)
    onestep=ways(stairs-1)
    return twostep+onestep
stairs=int(input("Enter number of stairs"))
print("Number of ways is ",ways(stairs))
