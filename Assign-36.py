
#A1
def removeDuplicates(mylist):
    return list(set(mylist))

#A2
def frequencyDict(mylist):
    d1={}
    i=0
    while i<len(mylist):
        if mylist.index(mylist[i])==i:
            f=mylist.count(mylist[i])
            d1[mylist[i]]=f

        i+=1
    return d1
#print(frequencyDict([10,20,10,30,20,10,10,20]))
#A3

def extractNumbersFromText(text):
    num=[]
    for word in text.split(' '):
        try:
            x=float(word)
            num.append(float(word))
        except:
            pass
    return num

#print(extractNumbersFromText("Sum of 3 and 4 is 7"))


#A4 |
l1=[3,4,8,11,22,30,2,5,7,9,1,6]
def largestSortedSubsequence(mylist):
    i=0
    j=0
    maxLength=-1
    while j <len(mylist):
        i=j
        j=i
        
        while j<len(mylist) and sorted(mylist[i:j+1])==mylist[i:j+1]:
            
            j+=1
        if j-i>maxLength:
            maxLength=j-i
            startIndex=i
            endIndex=j
    return (mylist[startIndex:endIndex])
#print(largestSortedSubsequence(l1))
#A5 | 

def compareList(l1,l2):
    return sorted(l1)==sorted(l2)

print(compareList([1,2,3,4],[5,4,1,3]))
print()
