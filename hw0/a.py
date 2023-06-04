import sys
from collections import defaultdict


counter = defaultdict(int)
max_count = 0

for line in sys.stdin:
	for c in line.strip():
		if c != " ":
			counter[c] += 1
			max_count = max(max_count, counter[c])
		

items = sorted(counter.items())



n = len(items)

for ri in range(max_count, 0, -1):
	ans = []
	for i in range(0, n):
		count = items[i][1]
		ans.append('#' if ri <= count else ' ')
	print(''.join(ans))
	
print(''.join(items[i][0] for i in range(n)))
