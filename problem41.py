num_sets = int(input())

median_nums = []

for i in range(0, num_sets):
    for line in input().split("\n"):
        nums = list(map(int, line.split()))
        nums.sort()
        median = nums[1]
        median_nums.append(median)

print(" ".join(map(str, median_nums)))
