import math


def to_celsius(f):
    c = (f - 32) * 5/9
    return c


def round(t):
    if t % 1 >= 0.5:
        return math.ceil(t)
    else:
        return math.ceil(t//1)


input_data = input().split()
converted_temps = []

for i in range(1, len(input_data)):
    temp_f = int(input_data[i])
    temp_c = to_celsius(temp_f)
    converted_temps.append(round(temp_c))

print(" ".join(map(str, converted_temps)))
