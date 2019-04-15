fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File can not be opened:',fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('s'):
        count = count + 1
print('There were ',count, 'lines starts with s in',fname)    
    