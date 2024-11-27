scores = {"Alice": 85, "Bob": 75, "Charlie": 95}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1]))
print(sorted_scores)
