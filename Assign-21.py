#Q1
'''
n = int(input("Enter a number:"))
for i in range(1, n+1):
    print(2*i)

#Q2
n = int(input("Enter a number:"))
for i in range(1, n+1):
    print(2*i-1)


#Q3
n = int(input("Enter a number:"))
for i in range(1, n+1):
    print(i**2)

#Q4
n = int(input("Enter a number:"))
for i in range(1, n+1):
    print(i**3)

'''
beg =15 
end = 45
for i in range(beg , end+1):
    for n in range(2,i):
        if i%n == 0:
            break
    else:
        print(i)

    
   