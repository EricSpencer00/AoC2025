# joltage from 1 -> 9
# find two batteries that sum total bank (line)
# 12345, 2 and 4 = 24
# find largest possible joltage in each bank

# import /inputs/d3_input.txt
# each line is a bank of batteries
with open('inputs/d3_input.txt') as f:
    lines = f.read().strip().splitlines()

'''
but now, we have a new constraint, the max voltage is not two digits, but twelve
so now we have to find the max twelve digit joltage
'''

# total_joltage = 0
# for line in lines:
#     max_joltage = 0
#     length = len(line)
#     for i in range(length):
#         for j in range(i + 1, length):
#             for k in range(j + 1, length):
#                 for l in range(k + 1, length):
#                     for m in range(l + 1, length):
#                         for n in range(m + 1, length):
#                             for o in range(n + 1, length):
#                                 for p in range(o + 1, length):
#                                     for q in range(p + 1, length):
#                                         for r in range(q + 1, length):
#                                             for s in range(r + 1, length):
#                                                 for t in range(s + 1, length):
#                                                     joltage = int(line[i] + line[j] + line[k] + line[l] + line[m] + line[n] + line[o] + line[p] + line[q] + line[r] + line[s] + line[t])
#                                                     if joltage > max_joltage:
#                                                         max_joltage = joltage
#     total_joltage += max_joltage

total_joltage = 0
for line in lines:
    length = len(line)
    digits_needed = 12
    pos = 0
    chosen_digits = []
    for d in range(digits_needed):
        # Remaining digits to pick after this one
        remaining = digits_needed - len(chosen_digits) - 1
        # We can only pick from pos to (length - remaining - 1)
        max_digit = '-1'
        max_idx = -1
        for idx in range(pos, length - remaining):
            if line[idx] > max_digit:
                max_digit = line[idx]
                max_idx = idx
        if max_idx == -1:
            break  # Not enough digits left
        chosen_digits.append(max_digit)
        pos = max_idx + 1
    if len(chosen_digits) == digits_needed:
        joltage = int(''.join(chosen_digits))
    else:
        joltage = 0
    total_joltage += joltage

print(total_joltage)