prices = {"apple": 3, "banana": 2, "cherry": 5}
max_price = max(prices, key=prices.get)
print(max_price)
