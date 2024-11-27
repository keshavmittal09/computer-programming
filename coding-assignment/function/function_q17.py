def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

print(safe_divide(10, 2))
print(safe_divide(10, 0))
