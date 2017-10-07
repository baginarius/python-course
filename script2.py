def celsToFahr(cels):
    r= 32 + 1.8*cels;
    return r

def c_to_f(c):
    f=c*9/5+32
    return f

print (celsToFahr(0));
print (celsToFahr(32));

print (c_to_f(0));
print (c_to_f(32));
