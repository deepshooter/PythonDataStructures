ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

print('\n')
print('-----------------')
print('\n')

counts = dict()
names = ['csev','cwen','csev','zyan','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]  =counts[name]+1
print(counts)        