def calculate(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/':
            a = tokens[i-1]
            b = tokens[i+1]
            if tokens[i] == '*':
                result = a * b
            else:
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = a / b
            tokens[i-1:i+2] = [result]
        else:
            i += 1
    i = 0
    while i < len(tokens):
        if tokens[i] == '-' or tokens[i] == '+':
            a = tokens[i-1]
            b = tokens[i+1]
            if tokens[i] == '+':
                result = a + b
            else:
                result = a - b
            tokens[i-1:i+2] = [result]
        else:
            i += 1
    return tokens[0]
