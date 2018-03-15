import math

num_sets = int(input())

results = []

for i in range(0, num_sets):
    for line in input().split("\n"):
        a, b = map(int, line.split())

        quotient = a / b
        remainder = quotient % 1

        if remainder >= 0.5:
            rounded_num = math.ceil(quotient)
        else:
            rounded_num = a // b

        #print(quotient, rounded_num)
        results.append(rounded_num)

print(" ".join(map(str, results)))
