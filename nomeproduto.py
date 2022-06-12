
print('---====Lista de Produtos====---')
print('* 1 - Pizza                   *')
print('* 2 - Hamburguer              *')
print('* 3 - Esfiha                  *')
print('* 4 - Batata                  *')
print('===============================')
produto = int(input('digite o código do produto: '))
if produto == 1:
    print('Você comprou Pizza')
elif produto == 2:
    print('Você comprou Hamburguer')
elif produto == 3:
    print('Você comprou Esfiha')
elif produto == 4:
    print('Você comprou batata')
else: 
    print('Desculpe. Este código não foi registrado ainda.')
