#A1
def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)


#A2
def sumOddN(n):
    if n==1:
        return 1
    return 2*n-1+sumOddN(n-1)
        

#A3
def sumEvenN(n):
    if n==1:
        return 2
    return 2*n+sumEvenN(n-1)


#A4 |

def sumSquareN(n):
    if n==1:
        return 1
    return n**2+sumSquareN(n-1)
        

#A5 | 
def sumCubeN(n):
    if n==1:
        return 1
    return n**3+sumCubeN(n-1)
print()
