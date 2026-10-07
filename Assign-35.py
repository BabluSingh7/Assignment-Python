#Q1
'''
def Lcm(a,b):
    L = a if a<b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            break
        L+=1
    return L
print(Lcm(4,8))

#Q2
def Count_word(s):
    c= 1
    for s1 in s:
        if s1 == ' ':
            c+=1
    return c

print(Count_word('my name is bablu singh'))

#Q3
def prime(a,b):
    l1=[]
    beg = a if a<b else b
    for n in range(beg,b):
        for i in range(2,n):
            if n%i==0:
                break
        else:
            l1.append(n)
    print(l1)
prime(15,45)
'''
#Q4
'''
def filterWord(text):
    alph = "abcdefghijklmnopqrstuvwxyz"
    d1 ={}
    for ch in alph:
        l1 =[word for word in text.split(' ') if word.startswith(ch)]
        if (len(l1)>0):
            d1[ch]=l1
    return d1

print(filterWord(input("Enter some text")))
'''
#A5 | 
def commonFactors(a,b):
    l1=[]
    f=a if a<b else b
    while f>=1:
        if a%f==0 and b%f==0:
            l1.append(f)
        f-=1
    return tuple(l1)
print(commonFactors(20,100))
print()

        