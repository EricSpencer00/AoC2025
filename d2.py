import re

def is_repeated_digits(n):
	s = str(n)
	l = len(s)
	if l % 2 != 0:
		return False
	half = l // 2
	return s[:half] == s[half:]

def main():
	with open('inputs/d2_input.txt') as f:
		line = f.read().strip()
	ranges = [r for r in line.split(',') if r]
	invalid_ids = []
	for r in ranges:
		start, end = map(int, r.split('-'))
		for n in range(start, end + 1):
			if is_repeated_digits(n):
				invalid_ids.append(n)
	print(sum(invalid_ids))

if __name__ == '__main__':
	main()
