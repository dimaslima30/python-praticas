a = int(input())
b = int(input())
c = int(input())
MaiorAB = int((a+b+abs(a-b))/2)
if c>MaiorAB:
    print(c, 'eh o maior')
else:
    print(MaiorAB, 'eh o maior')