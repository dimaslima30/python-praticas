num1 = float(input('digite um número: '))
num2 = float(input('digite outro número: '))
num3 = float
op = input('escolha uma operação: ')
if op == '*':
    num3 = num1 * num2
    if num3 >= 0:
        print('o resultado é %.2f' % num3, '| Positivo')
    else:
        print('o resultado é %.2f' % num3, '| Negativo!')
if op == '+':
    num3 = num1 + num2
    if num3>=0:
        print('o resultado é %.2f' % num3, '| Positivo')
    else:
        print('o resultado é %.2f' % num3, '| Negativo!')
if op == '-':
    num3 = num1 - num2
    if num3>=0:
        print('o resultado é %.2f' % num3, '| Positivo')
    else:
        print('o resultado é %.2f' % num3, '| Negativo!')
if op == '/':
    num3 = num1/num2
    if num3>=0:
        print('o resultado é %.2f' % num3, '| Positivo')
    else:
        print('o resultado é %.2f' % num3, '| Negativo!')
