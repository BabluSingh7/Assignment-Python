#Q1
l1=[int(e) for e in input("Enter numbers separated by comma: ").split(',')]

print(sum(l1))

#Q2
l1=[int(e) for e in input("Enter numbers separated by comma: ").split(',')]
avg=sum(l1)/len(l1)
print(avg)

#Q3
l1=[int(e) for e in input("Enter numbers separated by comma: ").split(',')]

l2=[x**2 for x in l1]
print(l2)

#Q4
l1=[int(e) for e in input("Enter numbers separated by comma: ").split(',')]
l1.sort(reverse=True)
print(l1)

#Q5
l1=[int(e) for e in input("Enter numbers separated by comma: ").split(',')]
l2=[x for x in l1[1::2]]
print(l2)