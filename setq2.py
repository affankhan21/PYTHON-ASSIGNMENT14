set11={1,2,3,4,5}
set12={4,5,6,7,8}
print("ORIGINAL SETS ARE : ")
print(set11)
print(set12)
print("REMOVE THE INTERSECTION :")
for i in set11 & set12:
    set11.remove(i)
print("AFTER REMOVING INTERSECTION SETS ARE :")
print(set11)
print(set12)    