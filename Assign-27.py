#Q1
'''
s = input("Enter a string: ")
words = s.split()
for i in range(len(words)-1,-1,-1):
    print(words[i], end=" ")
'''
#Q2
s=input("Enter a string: ")
print([eval(x) for x in [e for e in s.split(' ') if e!=''] if x.isdigit() or not x.isalpha() and type(eval(x))==float])

#Q3
s = input("Enter a string: ")
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#Q4
s = input("Enter a string: ")
print(s.upper())

#Q5
s = input("Enter a string: ")   
l1 = [e for e in s.split(' ') if e != '']
lengths = [ len(x) for x in l1]
print(l1[lengths.index(max(lengths))])



