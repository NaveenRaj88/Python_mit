__author__ = 'anandran'

# def f(x):
#     import math
#     return 10*math.e**(math.log(0.5)/5.27 * x)
#
# def f(x):
# 	import math
# 	return 150*math.e**(math.log(0.5)/32.2 * x)
#


def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)


# def radiationExposure(start, stop, step):
#     if(start == stop):
#         return 0
#     return (f(start)*step) + radiationExposure(start+step,stop,step)

def radiationExposure(start, stop, step):
    totalRadiationExposed = 0.0
    while start < stop :
        totalRadiationExposed = totalRadiationExposed + (f(start)*step)
        start = start+step
    return totalRadiationExposed


print radiationExposure(0, 3, 0.1)

# print(radiationExposure(0, 40, 1))
#
#
# print radiationExposure(0,5,1)
#
# print radiationExposure(5,11,1)
#
# radiationExposure(0,11,1)
#
# print radiationExposure(40,100,1.5)
#
# print radiationExposure(4,10,0.5)