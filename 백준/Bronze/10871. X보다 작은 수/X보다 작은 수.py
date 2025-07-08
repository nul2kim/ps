line = input().split(" ")
N = int(line[0])
X = int(line[1])

number = input().split()

for i in number:
    i=int(i)
    if i < X:
        print(i, end=' ')
