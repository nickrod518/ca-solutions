num_sets = int(input())

min_nums = []

for i in range(0, num_sets):
    for line in input().split("\n"):
        a, b, c = map(int, line.split())

        if a < b and a < c:
            min_nums.append(a)
        elif b < a and b < c:
            min_nums.append(b)
        else:
            min_nums.append(c)

print(" ".join(map(str, min_nums)))
