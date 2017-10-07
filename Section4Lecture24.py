def celsToFahr(cels):
    if cels < -273.15:
        return "invalid parameter"
    else:
        r= 32 + 1.8*cels
        return r


print (celsToFahr(0))
print (celsToFahr(-332))

w = "1234"
for i in w[0:2]:
    print(i)

lst=["Terribly Tricky"]
for word in lst:
    for letter in word[0:6]:
        print(letter)