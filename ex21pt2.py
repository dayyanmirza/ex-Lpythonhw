def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b} ")
    return a / b

# 24 + 34 / 100 - 1023 

age = add(24, 34)
weight = subtract(100, 1023)
result = divide(age, weight)

print(f"This is the overall results of dividing the age and weight: ", result)