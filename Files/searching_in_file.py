fhand = open('demo.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('s'):
        print(line)