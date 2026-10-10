#A1
isEven=lambda n: True if n%2==0 else False


#A2

fib=lambda n: n if n==0 or n==1 else fib(n-1)+fib(n-2)
#print(fib(10))
        
#A3
area=lambda r: 3.14*r*r
#print("Area of circle is",area(5))


#A4 |

hcf=lambda a,b: (b if a%b==0 else hcf(a%b,b)) if a>b else (a if b%a==0 else hcf(a,b%a))
#print(hcf(120,150))

#A5 | 

word_count=lambda text: len(text.split(' '))
#t="Mysirg Education Services Private Limited"
#print(word_count(t))
print()
