# joltage from 1 -> 9
# find two batteries that sum total bank (line)
# 12345, 2 and 4 = 24
# find largest possible joltage in each bank

# import /inputs/d3_input.txt
# each line is a bank of batteries
with open('inputs/d3_input.txt') as f:
    lines = f.read().strip().splitlines()

total_joltage = 0
for line in lines:
    # find max joltage for each line
    # we can't rearrange batteries, 
    '''
    in this line: 3443334373333545324339252335233845533545245422755419334136447332543353734352333342352363164324383844
    we can only use batteries in order
    the max would be two digits: 99
    '''
    max_joltage = 0
    length = len(line)
    for i in range(length):
        for j in range(i + 1, length):
            joltage = int(line[i] + line[j])
            if joltage > max_joltage:
                max_joltage = joltage
    total_joltage += max_joltage

print(total_joltage)