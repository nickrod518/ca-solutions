num_arrays = int(input())

sums = []

for i in range(0, num_arrays):
    for line in input().split("\n"):
        a, b = map(int, line.split())
        sums.append(a + b)


print(" ".join(map(str, sums)))
