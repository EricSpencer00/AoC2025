# database operates via ingredient IDs, list of fresh ingredient ID ranges, a blank line,
# and then a list of available ingredient IDs

'''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''
# 3-5 means that 3, 4, 5 are fresh
# determine which available ingredient IDs are fresh

# We need to join the ranges of fresh ingredient IDs with the available ingredient IDs

with open('inputs/d5_input.txt') as f:
    # use splitlines() (not strip) so an internal blank line is preserved
    content = f.read().splitlines()

def count_fresh():
    fresh_ranges = []
    available_ids = []
    reading_ranges = True

    for line in content:
        if line.strip() == "":
            reading_ranges = False
            continue
        if reading_ranges:
            start, end = map(int, line.split('-'))
            fresh_ranges.append((start, end))
        else:
            available_ids.append(int(line))

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

    # For fast membership checks, use bisect on starts
    import bisect
    starts = [iv[0] for iv in merged]
    ends = [iv[1] for iv in merged]

    count = 0
    for aid in available_ids:
        i = bisect.bisect_right(starts, aid) - 1
        if i >= 0 and ends[i] >= aid:
            count += 1

    return count

if __name__ == '__main__':
    print(count_fresh())