text = "apple banana apple orange banana apple"
words = text.split()
counts = {word: words.count(word) for word in set(words)}
print(counts)
