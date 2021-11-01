import math

a = -1
b = 0

h = 0.01

u_a = 1
du_a = 0


def f1(x, u_1=None, u_2=None):
    #if a <= x and x <= b:
        #return math.cos(pow(x, 3) / 3)
    return x
    #return u_2
    #return None

def f2(x, u_1, u_2):
    #if a <= x and x <= b:
        #return -2*x*math.sin(pow(x, 3) / 3) - pow(x, 4) * math.cos(pow(x, 3) / 3)
    #return 2 * u_2 / x - pow(x,4) * u_1
    return - u_2 - u_1 / x
    #return None
