line_count = int(input())

results = []

for input_line in range(0, line_count):
    for line in input().split("\n"):
        a, b, c = map(int, line.split())
        calc = str(a*b + c)

        nums = []

        for i in range(0, len(calc)):
            nums.append(int(calc[i]))

        results.append(sum(nums))

print(" ".join(map(str, results)))
