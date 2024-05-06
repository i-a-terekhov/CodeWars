def parse_expr(s):
    s = s[1:-1] if s[0] == '(' else s
    if s.isdigit():
        return ('num', int(s))
    elif ' ' not in s:
        return ('var', s)
    depth = 0
    first_space = s.index(' ')
    op = s[:first_space]
    for i, c in enumerate(s[first_space + 1:]):
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        if depth == 0 and c == ' ':
            second_space = first_space + i + 1
            return op, parse_expr(s[first_space + 1:second_space]), parse_expr(s[second_space + 1::])
    return op, parse_expr(s[first_space + 1:])


def deriv(expr):
    op, a, b = expr + ((None,) if len(expr) < 3 else ())
    return {
        'num': lambda: ('num', 0),
        'var': lambda: ('num', 1),
        '+': lambda: ('+', deriv(a), deriv(b)),
        '-': lambda: ('-', deriv(a), deriv(b)),
        '*': lambda: ('+', ('*', deriv(a), b), ('*', a, deriv(b))),
        '/': lambda: ('/', ('-', ('*', deriv(a), b), ('*', a, deriv(b))), ('^', b, ('num', 2))),
        'exp': lambda: ('*', deriv(a), ('exp', a)),
        'tan': lambda: ('*', deriv(a), ('+', ('num', 1), ('^', ('tan', a), 2))),
        'sin': lambda: ('*', deriv(a), ('cos', a)),
        'cos': lambda: ('*', deriv(a), ('*', ('num', -1), ('sin', a))),
        'ln': lambda: ('/', deriv(a), a),
        '^': lambda: ('*', ('*', ('num', b[1]), ('^', a, ('num', b[1] - 1))), deriv(a)) if b[0] == 'num' else (
        '*', expr, deriv(('*', b, ('ln', a))))
    }.get(op)()


def simplify(expr):
    op, a, b = expr + ((None,) if len(expr) < 3 else ())
    if type(a) == type(()): a = simplify(a)
    if type(b) == type(()): b = simplify(b)
    if op in ('num', 'var'):
        return a
    elif op == '*' and 0 in (a, b):
        return 0
    elif op == '^' and b == 1:
        return a
    elif op == '^' and b == 0:
        return 1
    elif op == '*' and 1 in (a, b):
        return a * b
    elif op == '+' and 0 in (a, b):
        return a if a else b
    elif op == '-' and b == 0:
        return a
    elif type(a) == type(b) == int:
        return calc(op, a, b)
    else:
        return (op, a) + ((b,) if b else ())


def calc(op, a, b):
    return {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b}.get(op)


def to_str(expr):
    return str(expr).replace(',', '').replace('\'', '')


def diff(expr):
    return to_str(simplify(deriv(parse_expr(expr))))
