def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    print("Simple Calculator")
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))
    print("Multiplication:", multiply(6, 7))
    print("Division:", divide(8, 2))
