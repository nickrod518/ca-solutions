def health(weight, height):
    BMI = weight / height**2

    if BMI < 18.5:
        return"under"
    elif BMI >= 18.5 and BMI < 25.0:
        return"normal"
    elif BMI >= 25.0 and BMI < 30.0:
        return "over"
    elif BMI <= BMI:
        return "obese"


sets = int(input())

health_report = []

for i in range(0, sets):
    for line in input().split("\n"):
        nums = list(map(float, line.split()))
        w = nums[0]
        h = nums[1]

        health_report.append(health(w, h))

print(" ".join(map(str, health_report)))
