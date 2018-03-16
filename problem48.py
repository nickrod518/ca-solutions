def collatz(num):
    next_num = None
    if num % 2 == 0:
        next_num = num/2
    else:
        next_num = 3*num + 1

    return next_num


num_sets = int(input())
input_data = list(map(int, input().split()))

collatz_terms = []

for num in input_data:
    print(num)
    terms = 0

    while num > 1:
        num = collatz(num)
        terms = terms + 1

    collatz_terms.append(terms)

print(" ".join(map(str, collatz_terms)))
