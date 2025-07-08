import sys

T = int(sys.stdin.readline())

for i in range(T):
    line = sys.stdin.readline().split(" ")
    a = int(line[0])
    b = int(line[1])

    if a <= 1000 and b <= 1000:
        print(a + b)
