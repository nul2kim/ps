x = int(input())
y = int(input())

if x > 0:  # x가 양수
    if y > 0:  # y가 양수
        print(1)
    else:  # y가 음수
        print(4)
else:  # x가 음수
    if y > 0:
        print(2)
    else:
        print(3)
