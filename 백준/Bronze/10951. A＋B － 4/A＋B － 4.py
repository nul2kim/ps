while True:
    try:
        line = input(). split()
        a = int(line[0])
        b = int(line[1])
        print(a + b)
    except EOFError:
        break
