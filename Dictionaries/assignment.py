name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    if len(wds) < 4 or wds[0] != 'From':
        continue
    email = wds[1]
    di[email] = di.get(email,0)+1
        
       
largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v 
        theword = k
        
print(theword,largest)        

       
       