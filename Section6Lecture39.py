def celsToFahr(cels, file):
    if cels < -273.15:
        print("That temperature doesn't make sense!")
    else:
        r= 32 + 1.8*cels
        file.write(str(r))
        file.write('\n')

temperatures=[10,-20,-289,100]
file = open('temperature.txt','w')
for t in temperatures:
    celsToFahr(t, file)

file.close()

