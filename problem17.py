num_sets = int(input())
input_data = list(map(int, input().split()))

checksum = 0

for num in input_data:
    checksum = (checksum + num)*113 % 10000007

print(checksum)
