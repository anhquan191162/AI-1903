c = {'a': 10, 'b':1, 'c':22}
tmp = []
for k,v in c.items():
    tmp.append((k, v))

print(tmp)

tmp = sorted(tmp, reverse= True)
print(tmp)