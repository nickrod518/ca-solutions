def triangle(a, b, c):
    # triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        return 1
    else:
        return 0


sets = int(input())
results = []

for i in range(0, sets):
    for line in input().split("\n"):
        a, b, c = map(int, line.split())
        results.append(triangle(a, b, c))

print(" ".join(map(str, results)))
