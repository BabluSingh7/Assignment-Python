#Q1
'''
l = [20,4.5,'abc',3+4j,True,30,40]

i=0
l2=[]
while(i<len(l)):
    if type(l[i]) ==int:
        l2.append(l[i])
    i +=1
print(l2)


#Q2
l = [1,2,3,4,2,3,5,6,7,5]
i =0
for x in l:
    if i==l.index(x):
        print(x,' ',l.count(x)) 
    i+=1


#Q3
l1 =["Bhopal","Indore","Jabalpur","Gwalior","Ujjain","Itarsi"]
l1.sort()
print(l1)


#Q4
l1 = ["AB","BC","BC","CD","DE","FG","HK","DE"]
i=0
for s in l1:
    if l1.index(s)!=i:
        print("first repeted string ",s,"at index ",i)
        break
    i+=1
'''
#Q5
l1 =["Places","white","fly","walk","pastries","royal","gags"]
count = 0
for s in l1: 
    if s.endswith('s'):
        count+=1
print(count)    
