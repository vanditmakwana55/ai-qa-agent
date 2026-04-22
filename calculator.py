class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a - b  # ❌ BUG: should be +
        self.history.append(result)
        return result

    def subtract(self, a, b):
        result = a + b  # ❌ BUG: should be -
        self.history.append(result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(result)
        return result

    def divide(self, a, b):
        if b == 0:
            return 0  # ❌ BUG: should raise error
        result = a / b
        self.history.append(result)
        return result

    def average(self):
        total = sum(self.history)
        return total / len(self.history)  # ❌ BUG: crash if empty

    def last_result(self):
        return self.history[-1]  # ❌ BUG: crash if empty

    def clear_history(self):
        self.history == []  # ❌ BUG: wrong operator

    def power(self, a, b):
        return a * b  # ❌ BUG: should be a ** b

    def percentage(self, part, whole):
        return (part / whole) * 100  # ❌ BUG: divide by zero risk

    def max_value(self, numbers):
        max_val = 0
        for num in numbers:
            if num > max_val:
                max_val = num
        return max_val  # ❌ BUG: fails for negative numbers

    def min_value(self, numbers):
        min_val = 0
        for num in numbers:
            if num < min_val:
                min_val = num
        return min_val  # ❌ BUG: fails for positive-only lists