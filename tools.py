operators = ('¬', '→')
numbers = '0123456789'


def generate_table(n):
    if n == 0:
        yield ()
    else:
        for digit in range(2):
            for row in generate_table(n-1):
                yield (digit,) + row

def is_sequence_correct_and_all_names_of_values(string):
    string = string.replace(' ', '')
    if not string:
        return False
    number_of_braces = 0
    number_of_implications = 0
    names_of_values = set()
    new_name = ''
    string = '(' + string
    string += ')'
    for i in range(1, len(string)):
        a, b = string[i-1], string[i]
        if b in numbers:
            if not new_name:
                new_name = 'x' + b
            else:
                new_name += b
            if a not in 'x' + numbers:
                return False

        elif new_name:
            names_of_values.add(new_name)
            new_name = ''
        
        if a == '→':
            number_of_implications +=1
            if b not in '¬(x':
                return False

        elif a == '¬':
            if b not in '¬(x':
                return False

        elif a == 'x':
            if b not in numbers:
                return False

        elif a == '(':
            if b not in '(¬x':
                return False
            number_of_braces += 1
            if number_of_implications == 1:
                number_of_implications = 0

        elif b == ')':
            if a not in ')' + numbers:
                return False
            number_of_braces -= 1
            if number_of_implications == 1:
                number_of_implications = 0

        elif b not in '(x¬→' + numbers or a not in ')' + numbers:
            return False

        if number_of_braces == -1:
            return False

        elif number_of_implications > 1:
            return False
    if not number_of_braces:
        return names_of_values, string
    else:
        return False

msg = """Алфавіт:
    xi - змінна, де x - символ, i - натуральне число
    ¬ - заперечення
    → - імплікація
Приклади формул:
    x154
    x1 → (x2 → x1)
    (x1 → (x2 → x3)) → ((x1 → x2)→(x1→x3))
    (¬x1 → ¬x2) → ((¬x1 → x2) → x1)
    ¬¬x1 → x1
    x1 → ¬¬x1
    ¬x1 → (x1 → x2)
    (x2 → x1) → (¬x1 → ¬x2)
    (x1 → (¬x1 →¬(x1→x2)))
    (x1 → x2) → ((¬x1 → x2)→x2)
Приклади не формул:
    F → H
    x1 → x2 → x3
    """
