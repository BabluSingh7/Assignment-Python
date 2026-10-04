#Q1

l1=[10,20,20,30,40,50,60]
print(set(l1))

#Q2
s = {10,20,38,44,8,45,78,56,7,23,43,71}
even = set()
odd = set()
s2 ={}
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(even ,"\n",odd)


#Q3
s1 ={"virat","Rohit","Rahul","Sachin","Kapil"}
i=0
for p1 in s1:
    i+=1
    for p2 in list(s1)[i::]:
        print(p1,p2)

#Q4
condidates ={"Arjun","Atishay","Priyam","Pankaj","Harish","Amit","Sohail","Rahul","Deepak","Rajesh","Gurpreet"}
black_hat_candidates={"Priyam","Deepak","Harish","Amit","Rahul","Rajesh"}
red_shoes_candidates={"Arjun","Pankaj","Priyam","Rahul","Gurpreet"}
s1=black_hat_candidates.intersection(red_shoes_candidates)
for c in s1:
    print(c)

#Q5
n = int(input("Enter a sum of dice number"))
s1 =set()
for i in range(1,7):
    for j in range(1,7):
        if i+j==n:
            s1.add((i+j))
print(s1)

