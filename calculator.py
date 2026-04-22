class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(result)
        return result

    def average(self):
        if not self.history:
            return 0
        return sum(self.history) / len(self.history)

    def last_result(self):
        return self.history[-1] if self.history else None

    def clear_history(self):
        self.history = []

    def power(self, a, b):
        result = a ** b
        self.history.append(result)
        return result

    def percentage(self, part, whole):
        if whole == 0:
            raise ValueError("Denominator cannot be zero")
        result = (part / whole) * 100
        self.history.append(result)
        return result

    def max_value(self, numbers):
        if not numbers:
            return None
        max_val = numbers[0]
        for num in numbers:
            if num > max_val:
                max_val = num
        return max_val

    def min_value(self, numbers):
        if not numbers:
            return None
        min_val = numbers[0]
        for num in numbers:
            if num < min_val:
                min_val = num
        return min_val