
str2=["yellow","white","purple","yellow","purple"]
uniqu=set(str2)
print(uniqu)
dict11={}
for i in uniqu:
    dict11[i]=str2.count(i)
print(dict11)    