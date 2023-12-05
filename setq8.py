str13 = ['restful', 'forty five', 'evil', 'over fifty', 'vile', 'fluster']
print("\nOriginal list of strings:")
print(str13)
res={}
for i in str13:
    sort=' '.join(sorted(i))
    if sort in res:
        res[sort].append(i)
    else:
        res[sort]=[i]
print(list(res.values()))             