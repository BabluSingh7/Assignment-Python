#Q1 

s = input("Enter a string: ")
for ch in s:
    if ch>= 'a' and ch <='z' or ch >= 'A' and ch <= 'Z':
        pass
    else:
        print("string has same characters other than alphabets")
        break
else:
    print("string has only alphabets")

#Q2
s = input("Enter a string:")
ch = input("Enter a character:")
if ch in s:
    print("{} is in the string {}".format(ch,s))
else:
    print("{} is not in the string {}".format(ch,s))

#Q3
s = input("Enter a string: ")
count =0
for v in s:
    if v in "aeiouAEIOU":
        count +=1
print("Vowel Count =",count)

#Q4
s = input("Enter a string: ")
space =1
for sp in s :
    if sp ==" ":
        space +=1
print("Total Words are",space)

#Q5

s = input("Enter a string: ")
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
