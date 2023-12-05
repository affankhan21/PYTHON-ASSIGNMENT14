list13=[1,4,6,2,3]
target=int(input("ENTER THE VALUE FOR TARGET :"))
res=[]
for i in range(len(list13)):
    for j in range(i+1,len(list13)):
        if(list13[i]+list13[j]==target):
            res.append((list13[i],list13[j]))
print(res)            
