fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x = line.rstrip()
    words = x.split()
    for y in words: 
        if y not in lst:
            lst.append(y)        
lst.sort()
print(lst)

    