import dynam

def f(x):
    return x*x

#print(dynam.orbit(f,3,8))

def mwdp(x):
    digits = [int(c) for c in str(x)]
    maxdigit = max(digits)
    numdigits = len(digits)
    return(x+maxdigit**numdigits)//2

print(dynam.orbit(mwdp,50,30))

#print(dynam.orbit_data(mwdp,50))
#print(dynam.eventual_period(mwdp, 50))
#print(dynam.steps_to_enter_cycle(mwdp, 50))
#print(dynam.eventual_cycle(mwdp,50))
#print(dynam.smallest_first([9,8,7,6,5,4,3,2,1]))