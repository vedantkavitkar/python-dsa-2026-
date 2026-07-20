li=int(input())
size=int(input("enter size of list:"))
for i in range(0,size):
    li.append(int(input()))
print(li) 
for i in li:
    if li.count(i)>1:
     li.remove(i) 
print(li)      
