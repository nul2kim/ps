N = int(input())

numbers=list(map(int,input(). split()))

V=int(input())

count = 0
for num in numbers:
    if num == V:
        count += 1

print(count)
