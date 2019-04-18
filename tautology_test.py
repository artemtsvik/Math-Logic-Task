from tools import *


def create_form_for_eval(st, expression):
    r = ''
    for name in st:
        r += '{} = Bool({}) \n'.format(name, '{}')
    r += 'r = ' + expression.replace('¬', '-').replace('→', '+')
    return r


class Bool:

    def __init__(self, value):
        self.value = value

    def __add__(a, b):
        if a.value == 1 and b.value == 0:
            return Bool(0)
        else:
            return Bool(1)

    def __neg__(self):
        if self.value == 1:
            return Bool(0)
        else:
            return Bool(1)

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    print(msg)
    print('='*79)
    while True:
        expression = input('Вираз: ')
        if expression in '01':
            break
        p = is_sequence_correct_and_all_names_of_values(expression)
        if p:
            names_of_values, form = p
            n = len(names_of_values)
            for tpl in generate_table(n):
                expression = form.replace('¬', '-').replace('→', '+')
                for name, value in zip(names_of_values, tpl):
                    expression = expression.replace(name, 'Bool(' + str(value) + ')')
                r = eval(expression)
                if r.value == 0:
                    example = expression.replace('-', '¬').replace('+', '→').replace('Bool', '')
                    print('Даний вираз не є тавтологією.')
                    print('Приклад:', example[1:-1])
                    break
            else:
                print('Даний вираз є тавтологією.')

        else:
            print('Синтаксична помилка: даний вираз не є формулою числення висловлювань.')
