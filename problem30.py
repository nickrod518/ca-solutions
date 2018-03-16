in_string = input()
rev_string = ""

for i in range(len(in_string) - 1, -1, -1):
    rev_string = rev_string + in_string[i]

print(rev_string)
