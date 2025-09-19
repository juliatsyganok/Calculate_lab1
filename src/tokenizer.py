def get_tokens(case):
    tokens = []
    i = 0
    while case[0].isspace():
        case = case[1:]
    while i < len(case):
        if case[i].isspace():
            i += 1
        elif case[i] in '+-':
            if i == 0 or case[i - 1] in '+-/*':
                j = i + 1
                while j < len(case) and (case[j].isdigit() or case[j] == '.'):
                    j += 1
                tokens.append(float(case[i:j]))
                i = j
            else:
                tokens.append(case[i])
                i += 1
        elif case[i] in '*/':
            tokens.append(case[i])
            i += 1
        elif case[i].isdigit() or case[i] == '.':
            # Собираем число
            j = i
            while j < len(case) and (case[j].isdigit() or case[j] == '.'):
                j += 1
            tokens.append(float(case[i:j]))
            i = j
    return tokens
