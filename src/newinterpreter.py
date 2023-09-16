# Define the necessary functions
def display(value):
    print(value)

def readnumber():
    return int(input())

def loopupto(n):
    return range(n)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def sub(a, b):
    return a - b

def divide(a, b):
    return a / b

# Define a function for interpreting the keywords
def interpret(code):
    for line in code.split('\n'):
        tokens = line.split()

        if tokens[0] == 'display':
            display(' '.join(tokens[1:]))

        elif tokens[0] == 'readnumber':
            result = readnumber()
            if len(tokens) > 1:
                var_name = tokens[1]
                globals()[var_name] = result

        elif tokens[0] == 'loopupto':
            n = int(tokens[1])
            for i in loopupto(n):
                globals()['i'] = i
                exec(' '.join(tokens[2:]))

        elif tokens[0] == 'define':
            func_name = tokens[1]
            func_args = tokens[2:-1]
            func_body = ' '.join(tokens[tokens.index('{')+1:])
            func_def = 'def {}({}):{}'.format(func_name, ', '.join(func_args), func_body)
            exec(func_def)

        elif tokens[0] == 'add':
            a = int(tokens[1])
            b = int(tokens[2])
            result = add(a, b)
            if len(tokens) > 3:
                var_name = tokens[3]
                globals()[var_name] = result
            else:
                display(result)

        elif tokens[0] == 'multiply':
            a = int(tokens[1])
            b = int(tokens[2])
            result = multiply(a, b)
            if len(tokens) > 3:
                var_name = tokens[3]
                globals()[var_name] = result
            else:
                display(result)

        elif tokens[0] == 'sub':
            a = int(tokens[1])
            b = int(tokens[2])
            result = sub(a, b)
            if len(tokens) > 3:
                var_name = tokens[3]
                globals()[var_name] = result
            else:
                display(result)

        elif tokens[0] == 'divide':
            a = int(tokens[1])
            b = int(tokens[2])
            result = divide(a, b)
            if len(tokens) > 3:
                var_name = tokens[3]
                globals()[var_name] = result
            else:
                display(result)




