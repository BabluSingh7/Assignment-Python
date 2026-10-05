#A1
def isEven(n):
    return n%2==0

#A2
def greater(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
    

#A3
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#A4
def isLeapYear(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        if year%4==0:
            return True
        else:
            return False

#A5
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


print(fact(5))
