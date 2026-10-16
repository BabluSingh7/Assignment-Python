
#A1
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)


#A2
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def getArea(self,radius):
        return 3.14*radius**2
    def getCircumference(self,radius):
        return 2*3.14*radius
#A3
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def setDimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimensions(self):
        print("Length=",self.length,"Breadth=",self.breadth)
    def getArea(self):
        return self.length*self.breadth

#A4 |
class Book:
    def __init__(self,id,title,price):
        self.bookid=id
        self.title=title
        self.price=price
    def show(self):
        print(self.bookid,self.title,self.price)
#A5 |

class Team:
    def __init__(self):
        self.teamMemberNames=[] 
    def inputMembers(self):
        print("Enter Member names separated by comma")
        self.teamMemberNames=input().split(',')
    def displayMembers(self):
        for name in self.teamMemberNames:
            print(name)
t1=Team()
t1.inputMembers()
t1.displayMembers()
     
print()
