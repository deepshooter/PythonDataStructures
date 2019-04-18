name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    if len(wds) < 4 or wds[0] != 'From':
        continue
    time = wds[5]
    temp = time.split(':')
    hr = temp[0]
    di[hr] = di.get(hr,0)+1
       

  
tmp = list()
for k,v in di.items():
    newtup = (k,v)
    tmp.append(newtup)
    
      

tmp = sorted(tmp)


for v,k in tmp:
    print(v,k)


