def is_closed_brackets(expression):
    dict = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = []
    finished = False

    for char in expression:
        if char in '({[':
            stack.append(char)
        if char in ')}]':
            if not stack:
                result = 'Зайва закриваюча дужка'
                finished = True
                break
            if dict[stack.pop()] != char:
                result = 'Не співпадають закриваючі дужки'
                finished = True
                break

    if not finished:
        if stack:
            result = 'Є не закриті дужки'
        else:
            result = 'Усі дужки закриті правильно'

    return expression + ': ' + result

list = [
    '( ) { [ ] ([]{()} ) ( ) { } } ]',
    '( ){[ 1 ]( 1 + 3 )( ){ }}',
    '( 23 ( 2 - 3);',
    '( 11 }'
]

for example in list:
    print(is_closed_brackets(example))

