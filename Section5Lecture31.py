def celsToFahr(cels):
    if cels < -273.15:
        return "That temperature doesn't make sense!"
    else:
        r= 32 + 1.8*cels
        return r

temperatures=[10,-20,-289,100]

for t in temperatures:
    print(celsToFahr(t))

