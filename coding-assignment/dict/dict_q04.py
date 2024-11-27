data = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in data.items() if v % 2 == 0}
print(filtered)
