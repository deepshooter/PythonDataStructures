fhand = open('demo.txt')
for line in fhand:
    if line.startswith('to'):
        print(line)