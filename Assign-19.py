
#Q-1 corresponding string unicode
s = input("Enter a string \n")
for u in s:
    print(u,"=",ord(u))

#Q-2 print only vowels
v ='aeiouAEIOU'
s = input("Enter a string \n")
for u in s:
    if u in'aeiouAEIOU':
        print(u)

        
#Q-3 count Space in a given  string

s = input("Enter a string:")
count =0
for c in s:
    if c in " ":
        count = count+1
print("Number of space is = ",count)


#Q-4 print unique digit

s = input("Enter a number:")
u = ''
for ch in s:
    if ch not in u:
        u+=ch
print(u)




#Q-5 count number of digit
count=0
n = int(input("Enter a number \n"))
while n:
    r = n%10
    n = n//10
    count = count+1
print("Number of digit is = ",count)

