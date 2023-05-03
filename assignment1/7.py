itemp = int(input("enter intial temp "))
ftemp = int(input("enter final temp "))
weight= int(input("enter amount of water in kg "))
energy= weight*(ftemp-itemp)*4184
energy=round(energy,2)
print("energy in joules is ",energy)
