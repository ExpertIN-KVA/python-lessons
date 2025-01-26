# for loop
total = 0
for i in range(10, 100):
    if i % 2 != 0:
        continue

    total += i

print(total)


# while loop
total = 0
i = 10
while i < 100:
    print(i)
    i += 2
