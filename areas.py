a = round(float(input()), 1)
b = round(float(input()), 1)
c = round(float(input()), 1)
a = float(a)
b = float(b)
c = float(c)
Atriang = (a*c)/2
Acirc = 3.14159*(c*c)
Atrap = (c*(a+b))/2
Aquad = b*b
Aret = a*b

print('TRIANGULO: %.3f'%Atriang)
print('CIRCULO: %.3f'%Acirc)
print('TRAPEZIO: %.3f'%Atrap)
print('QUADRADO: %.3f'%Aquad)
print('RETANGULO: %.3f'%Aret)