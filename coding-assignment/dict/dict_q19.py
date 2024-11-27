items = ["a", "b", "a", "c", "b", "a"]
count = {}
for i in items:
    count[i] = count.get(i, 0) + 1
print(count)
