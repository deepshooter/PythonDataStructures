counts = dict()
names = ['csev','cwen','csev','zyan','cwen']

for name in names:
    counts[name] = counts.get(name,0)+1

print(counts)  
  