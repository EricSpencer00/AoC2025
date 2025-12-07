'''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
'''
# import inputs/d6_input.txt
with open('inputs/d6_input.txt') as f:
    content = f.read().splitlines()

def solve_worksheet():
    # Transpose the content to work column-wise
    if not content:
        return 0   
    num_cols = max(len(line) for line in content)
    cols = ['' for _ in range(num_cols)]
    for line in content:
        for i in range(num_cols):
            if i < len(line):
                cols[i] += line[i]
            else:
                cols[i] += ' '
    total = 0
    i = 0
    while i < num_cols:
        # Skip empty columns
        if all(c == ' ' for c in cols[i]):
            i += 1
            continue
        # Read a problem
        # Determine block start..end (columns for this problem)
        start = i
        while i < num_cols and not all(c == ' ' for c in cols[i]):
            i += 1
        end = i - 1

        # Extract rows for this block
        # The bottommost row (last line) contains the operator for the problem
        operator_row = content[-1]
        # But operator may be within block; find any '+' or '*' in the operator row slice
        op = None
        for ch in operator_row[start:end+1]:
            if ch in '+*':
                op = ch
                break

        # Numbers are all rows above the last row
        numbers = []
        for row in content[:-1]:
            snippet = row[start:end+1]
            val = snippet.strip()
            if val:
                # remove spaces inside snippet to get the full number
                numstr = ''.join(ch for ch in snippet if ch != ' ')
                if numstr:
                    numbers.append(int(numstr))

        if not numbers or not op:
            # nothing to compute
            continue

        if op == '+':
            result = sum(numbers)
        else:
            result = 1
            for n in numbers:
                result *= n
        total += result
    return total

print(solve_worksheet())