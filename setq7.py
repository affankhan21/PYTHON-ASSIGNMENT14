set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}
print("ORIGINAL SETS ARE:")
print(set1)
print(set2)
print("Missing numbers in the second set as compared to the first:")
a=set(set1)-set(set2)
print(a)
print("Missing numbers in the first set as compared to the second:")
b=set(set2)-set(set1)
print(b)
