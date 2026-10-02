#Q1
#l1 = [int(e) for e in input("Enter a number seperated by commas").split(',')]

'''
n = int(input("Enter a number:\n"))
l =[]
for x in range(1,n+1):
    l.append(2*x)
print(l)
   
#Q2
n = int(input("Enter a number:\n"))
l =[]
a,b=-1,1
for x in range(1,n+1):
    c = a+b
    l.append(c)
    a,b = b,c

print(l)


#Q3
n = int(input("Enter a number:\n"))
l =[]
for x in range(1,n+1):
    for n in range(2,x):
        if x%n==0:
            break
    else:
        l.append(x)

print(l)


#Q4
print("Enter values row wise for first matrix")
A=[]
for i in range(3):
    A.append([int(e) for e in input("Enter three numbers separated by comma: ").split(',')])

print("Enter values row wise for the second matrix")
B=[]
for i in range(3):
    B.append([int(e) for e in input("Enter three numbers separated by comma: ").split(',')])

C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        C[i][j]=A[i][j]+B[i][j]

for i in range(3):
    for j in range(3):
        print(C[i][j],end=' ')
    print()
'''
#Q5
l1=[int(e) for e in input("Enter numbers separated by comma: ").split(',')]
positive=[x for x in l1 if x>0]
non_positive=[x for x in l1 if x<=0]
print(positive)
print(non_positive)




