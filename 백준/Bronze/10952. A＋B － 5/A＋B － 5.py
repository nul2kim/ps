while True:
    line = input().split(' ')
    a = int(line[0])
    b = int(line[1])

    if a == 0 and b == 0:
        break

    print(a + b)