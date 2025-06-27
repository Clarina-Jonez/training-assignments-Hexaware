def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            # Pop last two values
            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)  # Integer division

    return stack.pop()

# Example usage
expr = "231*+9-"
result = evaluate_postfix(expr)
print("Postfix Result:", result)
