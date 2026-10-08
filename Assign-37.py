#Q1
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')

#printN(10)
#Q2

def printNR(n):
    if n>0:
        print(n,end=',')
        printNR(n-1)

#printNR(10)

#Q3
def printodd(n):
    if n >0:
        printodd(n-1)
        print(2*n-1,end=',')
#printodd(10)

#Q4
def printodd(n):
    if n >0:
        print(2*n-1,end=',')
        printodd(n-1)
#printodd(10)

#Q5
def printSt(n):
    if n>0:
        printSt(n-1)
        print("MysirG",end=' ')

printSt(10)




