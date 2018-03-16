cases = int(input())

results = []

for num in input().split():
    total = 0

    for i in range(0, len(num)):
        total = total + int(num[i])*(i + 1)

    results.append(total)

print(" ".join(map(str, results)))
