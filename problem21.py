m, n = map(int, input().split())

num_list = {}
results = []

for num in map(int, input().split()):
    if num in num_list:
        num_list[num] += 1
    else:
        num_list[num] = 1

for num in sorted(num_list):
    results.append(num_list[num])

print(" ".join(map(str, results)))
