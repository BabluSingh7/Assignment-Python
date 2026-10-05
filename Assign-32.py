#A1
def add(a,b):
    return a+b

#A2
def areaOfCircle(r):
    return 3.14*r**2

#A3
def average(a,b,c):
    return (a+b+c)/3

#A4
def compoundInterest(p,r,t):
    A=p*(1+r/100)**t
    return A-p

#A5
def volumeOfCuboid(l,b,h):
    return l*b*h

v =volumeOfCuboid(2,4,6)
print(v)
