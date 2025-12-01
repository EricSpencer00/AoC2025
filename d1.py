from pathlib import Path
import sys

# Read input from `d1_input.txt` by default, or from a file path passed as
# the first command-line argument.
input_path = Path('d1_input.txt')
if len(sys.argv) > 1:
    input_path = Path(sys.argv[1])
try:
    d1_input_text = input_path.read_text()
except Exception as e:
    raise SystemExit(f"Failed to read input file {input_path}: {e}")

# Dial numbers are 0..99
DIAL_SIZE = 100

# Start position
position = 50
# Count how many times the dial points at 0 after any rotation
zero_count = 0

for line in d1_input_text.strip().splitlines():
    if not line:
        continue
    direction = line[0]
    try:
        value = int(line[1:])
    except ValueError:
        raise SystemExit(f"Invalid input line: {line!r}")

    if direction == 'L':
        position = (position - value) % DIAL_SIZE
    elif direction == 'R':
        position = (position + value) % DIAL_SIZE
    else:
        raise SystemExit(f"Invalid direction in line: {line!r}")

    if position == 0:
        zero_count += 1

print(zero_count)