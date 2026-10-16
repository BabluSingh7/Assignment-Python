from  functools import reduce

#Q1
"""
def vowelcount(s):
    count =0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
    return count

def f1():
    l1 =["Bhopal","Jaipur","Mumbai","Kanpur"]

    for m in map(vowelcount,l1):
        print(m)
#f1()

#Q2
def countdigit(n):
    count =0
    while n:
        n=n//10
        count+=1
    return count

def f2():
    t =(123,45,3,1023,22334455)
    for m in map(countdigit,t):
        print(m)
f2()

#Q3
def f3():
    s1 ={3,56,78,21,39,45,10,16}
    x =int(input("Enter a number:"))
    print(list(filter(lambda n : n if n>x else None ,s1)))

f3()

#Q4

def f4():
    l1 =[12,34,3+5j,"Bablu",23.9,45.5]
    print(list(filter(lambda n : n if type(n)==int else None ,l1)))

f4()

"""
#Q5
def hcf(a,b):
    h = a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def f5():
    l1 =[200,160,150,90]
    print(reduce(hcf,l1))   

f5() 
    
    
