n1 = float(input('qual foi a primeira nota? '))
n2 = float(input('qual foi a segunda nota? '))
n3 = float(input('qual foi a terceira nota? '))
media = (n1+n2+n3)/3
if media >= 5:
    print('Parabéns! Você está aprovado com média %.2f' % media)
else:
    print('Poxa! Você está reprovado com média %.2f' % media)