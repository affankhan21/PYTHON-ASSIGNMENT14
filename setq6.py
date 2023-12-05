num13=[1,2,3,4,5,6,7,8,8,9,10,1,11,12,13,14]
print(num13)
print(len(num13))
set13=set(num13)
print(set13)
print(len(set13))
produ=0
max1=0
max2=0
for n1 in set13:
    for n2 in set13:
        if n1!=n2 and n1*n2>produ:
            max_product = n1 * n2
            max_num1 = n1
            max_num2 = n2
print(max_num1,max_num2)    