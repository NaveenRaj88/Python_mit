__author__ = 'anandran'

def iterPower(base, exp):
    result = 1
    while exp > 0:
        result = result * base
        exp = exp-1
    return result

def recurPower(base, exp):
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)

def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base , exp/2)
    else:
        return base * recurPowerNew(base,exp-1)


print recurPowerNew(3,4)


print iterPower(3,4)