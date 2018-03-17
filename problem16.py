sets = int(input())
results = []

for i in range(0, sets):
    for line in input().split("\n"):
        nums = list(map(int, line.split()))

        mean = sum(nums) / (len(nums) - 1)
        rounded_mean = round(mean)

        results.append(rounded_mean)

print(" ".join(map(str, results)))
