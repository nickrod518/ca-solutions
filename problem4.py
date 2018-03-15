num_sets = int(input())

min_nums = []

for i in range(0, num_sets):
    for line in input().split("\n"):
        a, b = map(int, line.split())

        if a < b:
            min_nums.append(a)
        else:
            min_nums.append(b)


print(" ".join(map(str, min_nums)))
