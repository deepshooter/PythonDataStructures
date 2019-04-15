fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('s'):
        count = count + 1
print('There were ',count, 'lines starts with s in',fname)          