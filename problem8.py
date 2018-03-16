sets = int(input())

results = []

for i in range(0, sets):
    for line in input().split("\n"):
        nums = list(map(int, line.split()))

        a = nums[0]
        b = nums[1]

        total = 0

        for n in range(0, nums[2]):
            total = total + (a + n*b)

        results.append(total)

print(" ".join(map(str, results)))
