fname = input("Enter file name: ")
fh = open(fname)
count = 0
totalCount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count+1
    pos = line.find(':')
    totalCount = totalCount + float(line[pos+2:])
avg = totalCount/count    
print('Average spam confidence: ',avg)