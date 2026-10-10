#Q1
def sumN(n):
    if n==0:
        return 0
    s = n%10+sumN(n//10)
    return s

print(sumN(123456))

#Q2
def fact(n):
    f=1
    if n==1:
        return 1
    f =f*n*fact(n-1)
    return f

print(fact(5))

#Q3
def binary(n):
    if n==0:
        return 0
    binary(n//2)
    print(n%2,end='')

binary(4)

#Q4
def octN(n):
    if n==0:
        return 0
    octN(n//8)
    print(n%8,end='')

octN(25)


#A5 | 
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def nextPrime(x):
    x+=1
    while not isPrime(x):
        x+=1
    return x

def nthPrime(n):
    
    x=1
    for i in range(1,n+1):
        x=nextPrime(x)
    return x
    

def primeSum(n):
    if n==0:
        return 0
    return primeSum(n-1) + nthPrime(n)

print(primeSum(5)) # 2 +3 +5 +7+11
print()

