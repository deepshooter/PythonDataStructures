name = input("Enter file:")
if len(name) < 1 : name = "romeo.txt"
handle = open(name)

di = dict()
for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0)+1
       

#print(di)   

tmp = list()
for k,v in di.items():
    newtup = (v,k)
    tmp.append(newtup)
    
    
#print('Flipped : ' , tmp)  

tmp = sorted(tmp,reverse=True)

#print('Sorted :' , tmp[:5])

for v,k in tmp[:5]:
    print(k,v)


