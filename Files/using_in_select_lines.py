fhand = open('demo.txt')
for line in fhand:
    line = line.rstrip()
    if not 'the' in line:
        continue
    print(line)    