#Q1

def avg(*t):
    return sum(t)/len(t)


print(avg(1,2,3,4))

#Q2
def greatest(*t):
    return max(t)

print(greatest(2,3,4,9,5,8,6,8))

#Q3

def filteroddEven(*t):
    l1=[]
    l2=[]
    for e in t:
        if e%2==1:
            l1.append(e)
        else:
            l2.append(e)
    return (l1,l2)

print(filteroddEven(2,3,4,5,67,8,9,1,10,11))

#Q4

def maxlengthstring(*t):
    max_length=0
    for s in t:
        if max_length<len(s):
            max_length =len(s)
    return [s for s in t if len(s)==max_length]

print(maxlengthstring("ab","abc","ab","abc","ac"))

#Q5

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True

def filterprime(*t):
    return [e for e in t if isprime(e)]
print(filterprime(2,3,4,5,6,7,8,9,10,11,12,23))