fhand = open('demo.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('s'):
        continue
    print(line)