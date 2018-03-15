max_num = None
min_num = None

for i in input().split():
    num = int(i)
    if max_num == None or min_num == None:
        max_num = num
        min_num = num
    else:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

print(max_num, min_num)
