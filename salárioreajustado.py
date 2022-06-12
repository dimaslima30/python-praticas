salario = float(input('Quanto você recebe?: R$'))
if salario < 300:
    print('Seu salário será reajustado para R$', salario*1.45)
elif salario > 300 and salario < 600:
    print('Seu salário será reajustado para R$', salario*1.25)
elif salario > 600:
    print('Seu salário será reajustado para R$', salario*1.15)
else:
    print('Desculpe. Entre com valores numéricos, por favor.')