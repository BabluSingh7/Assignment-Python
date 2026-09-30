#Q-1
x = int(input("Enter a number:"))
match x:
    case x if 1000>x>99:
        print(" 3 digit number")
    case x :
        print(" not 3 digit number")

#Q-2
x = int(input("Enter a number"))
match x:
    case x if x>0:
        print("positive number")
    case x if x<0:
        print("Negative")
    case x if x==0: 
        print("Zero")

#Q-3
print('' \
'1.even and odd' \
'2.positive or non positive' \
'3.Simple interst' \
'4.Find roots of quadratic Equestion')
c = int(input("Enter a number:"))
match c:
    case c if 1:
        n = int(input("Enter a number"))
        if n %2==0 :
            print("Even number")
        else:
            print("Odd number")
    case c if 2:
        n = int(input("Enter two number"))
        if n>0:
            print("positive number")
        else:
            print("Non positive number")
    case c if 3:
        p,r,t = int(input("Enter principle rate and time")),int(input()),int(input())
        si = (p*r*t)/100
        print("Simple interst is =",si)
    case c if 4:
        a,b,c = int(input("Enter value A ,B and C ")),int(input()),int(input())
        d = b**2 -4*a*c
        if d>0:
            print("Two real and distinct roots")
        elif d==0:
            print("Two real and equal roots")
        else:
            print("Two Imaginary roots")

#Q-4
x = eval(input("Enter same data"))
match x:
    case x if type(x) == int:
        print("Monday")
    case x if type(x) == float:
            print("Tuesday")
    case x if type(x) == complex:
            print("Wednesday")
    case x if type(x) == bool:
            print("Thursday")

#Q-5
x =(input("Enter same string"))
match x:
    case x if x in  "mysirG":
        print("one")
    case x if x in "education":
            print("Two")
    case x if x in "Services":
            print("three")
    

