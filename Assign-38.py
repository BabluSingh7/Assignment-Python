#Q1
def printEven(n):
    if n>0:
        printEven(n-1)
        print(2*n,end=' ')

#printEven(10)

#Q2
def printEvenR(n):
    if n>0:
        print(2*n-1,end=',')
        printEvenR(n-1)

#printEvenR(10)

#Q3
def printSquar(n):
    if n>0:
        printSquar(n-1)
        print(n**2,end=' ')

#printSquar(10)

#Q4
def printCube(n):
    if n>0:
        printCube(n-1)
        print(n**3,end=' ')

#printCube(10)

def GivenNR(n):
    if n>0:
        print(n%10,end='')
        GivenNR(n//10)

GivenNR(1234)
