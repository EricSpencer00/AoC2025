def find_x():
    with open('inputs/d5_input.txt') as f:
        # use splitlines() (not strip) so an internal blank line is preserved
        content = f.read().splitlines()

    fresh_ranges = []
    # Be robust: treat any line that contains a '-' as a fresh range.
    # Some inputs may omit the blank separator, so we don't rely on it.
    for line in content:
        s = line.strip()
        if not s:
            continue
        if '-' in s:
            start, end = map(int, s.split('-'))
            fresh_ranges.append((start, end))
        else:
            # non-range lines are ignored for Part Two
            continue

    # Merge overlapping/adjacent ranges to avoid expanding huge ranges
    fresh_ranges.sort()
    merged = []
    for s, e in fresh_ranges:
        if not merged:
            merged.append([s, e])
            continue
        last = merged[-1]
        if s <= last[1] + 1:
            # overlap or adjacent -> merge
            last[1] = max(last[1], e)
        else:
            merged.append([s, e])

    # Part Two: count total unique IDs covered by the merged fresh ranges
    total_fresh = 0
    for s, e in merged:
        total_fresh += (e - s + 1)

    return total_fresh

if __name__ == '__main__':
    print(find_x())
