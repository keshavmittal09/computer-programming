nested = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
flat = {f"{outer}_{inner}": value for outer, inner_dict in nested.items() for inner, value in inner_dict.items()}
print(flat)
