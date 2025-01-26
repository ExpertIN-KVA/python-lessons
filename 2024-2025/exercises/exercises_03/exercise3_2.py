num = int(input())

for i in range(1, num + 1):
    if num % i != 0:
        continue

    print(i)
