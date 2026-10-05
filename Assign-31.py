#Q1
'''
n = int(input("Enter a Number"))
d1 = {i:i**2 for i in range(1,n+1)}
print(d1)

#or 

d1={n:n**2 for n in range(1,int(input("Enter a number"))+1)}
print(d1)

#Q2
d2 ={n:n**2 for n in range(1,int(input("Enter a number"))+1)}
l1 = sorted(d2,reverse=True)
for k in l1:
    print(k,'',d2[k])

'''
#Q3
n = int(input("Enter how many player data you want to store"))
players ={}

for i in range(1,n+1):
    name =input("Enter the name of the players")
    print("Enter Numbers of Matches played")
    a=input()
    print("Total runs")
    b=input()
    print("Half Centuries")
    c=input()
    print("Centuries")
    d=input()
    players[name]=(a,b,c,d)
for k,v in players.items():
    print(k,v)

#A4

batches={
    'SA':200,
    'SB':189,
    'SC':207,
    'SD':305,
    'SE':280
}
max=0
batch_code=''
for k,v in batches.items():
    if(v>max):
        max=v
        batch_code=k
print("Max size batch code is",batch_code)



#A5
cities=[
    "Bhopal",
    "Indore",
    "Jabalpur",
    "Ujjain",
    "Gwalior",
    "Bikaner",
    "Jaipur",
    "Pune",
    "Patna",
    "Kanpur",
    "Panjim"
]
d={}
for alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    names=[]
    for city in cities:
        if city.startswith(alpha):
            names.append(city)
    if len(names)>0:
        d[alpha]=names
for k,v in d.items():
    print(k,v)

print()
