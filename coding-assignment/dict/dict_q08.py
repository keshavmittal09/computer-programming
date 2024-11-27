from collections import defaultdict
inventory = defaultdict(int)
inventory["apple"] += 5
inventory["banana"] += 2
print(dict(inventory))
