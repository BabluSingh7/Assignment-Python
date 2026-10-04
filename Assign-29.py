#Q1

l1 = [1,2,3,4,5,6,7]
t =tuple(l1)
print(t)

#Q2
t = (2,3,4,5,6,7,8)
for i in t[::-1]:
    print(i)

#Q3
l1=['bhopal','patna','pune','bharatpur','jaipur','jodhpur']
mylist=[]
temp=[]
alpha ="abcdefghijklmnopqrstuvwxyz"
l1.sort()

for i in range(0,26):
    temp.clear()
    for j in l1:
        if j.startswith(alpha[i]):
            temp.append(j)
    if len(temp)>0:
        mylist.append(tuple(temp))
print(mylist)

#Q4
mylist=[]
for i in range(65,91):
    mylist.append((chr(i),i))
print(mylist)

#Q5
t1 = (2,3,4,5,6,7,8,9,10,11,12,13)
s=0
for i in t1:
    if i%2==1:
        s+=i
print("Sum of odd numbers",s)
