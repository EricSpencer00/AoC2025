'''
The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
'''

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

        # For Part Two: each number is given in its own column (top->bottom digits).
        # Collect column-wise numbers, left-to-right, then read right-to-left.
        col_numbers = []
        for c in range(start, end + 1):
            col_chars = []
            for r in range(len(content) - 1):
                ch = content[r][c] if c < len(content[r]) else ' '
                col_chars.append(ch)
            numstr = ''.join(ch for ch in col_chars if ch != ' ')
            if numstr:
                col_numbers.append(int(numstr))

        # Read columns right-to-left as cephalopods do
        numbers = list(reversed(col_numbers))

        # Perform the operation
        if not numbers or not op:
            result = 0
        elif op == '+':
            result = sum(numbers)
        elif op == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            result = 0

        total += result
    return total

print(solve_worksheet())