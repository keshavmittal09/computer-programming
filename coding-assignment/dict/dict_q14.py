nums = {"a": 10, "b": 20, "a": 5}
sums = {}
for k, v in nums.items():
    sums[k] = sums.get(k, 0) + v
print(sums)
