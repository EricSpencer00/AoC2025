import re

def is_repeated_digits(n):
		s = str(n)
		l = len(s)
		# Try all possible chunk sizes from 1 up to half the length
		for size in range(1, l // 2 + 1):
			if l % size != 0:
				continue
			chunk = s[:size]
			if chunk * (l // size) == s:
				return True
		return False

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
