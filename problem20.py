line_count = int(input())

vowels = ["a", "o", "u", "i", "e", "y"]
results = []

for input_line in range(0, line_count):
    for line in input().split("\n"):
        vowel_count = 0

        for c in range(0, len(line)):
            letter = line[c]
            if letter in vowels:
                vowel_count = vowel_count + 1

        results.append(vowel_count)

print(" ".join(map(str, results)))
