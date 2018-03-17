import math


def dice_roll(num, sides=6):
    roll = math.floor(num * sides) + 1
    return roll


sets = int(input())
results = []

for i in range(0, sets):
    for line in input().split("\n"):
        results.append(dice_roll(float(line)))

print(" ".join(map(str, results)))
