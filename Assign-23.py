#Q1
'''
n = int(input("Enter a number: "))
f = 1
for i in range(1, n + 1):
    f *= i
print("Factorial of", n, "is:", f)

#Q2
n = int(input("Enter a number: "))
count =0
while n:
    n= n//10
    count+=1
print("Number of digits is :",count)

#Q3
n = int(input("Enter a number: "))
s =0
while n:
    r = n%10
    s = s+r
    n= n//10
print("Sum of digits is :",s)

'''
#Q4
n = int(input("Enter a number: "))
u =''
while n:
    r = n%2
    u = str(r)+u
    n = n//2
print("Binary of number is :",u)

#Q5
n = int(input("Enter a number: "))
u =''
while n:
    r = n%8
    u = str(r)+u
    n = n//8
print("Octal of number is :",u)
