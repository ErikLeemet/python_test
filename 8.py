a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a > b + c or b > a + c or c > a + b:
    print('sellist kolmnurka ei eksisteeri')
elif a == b and b == c:
    print('vordkulgne kolmnurk')
elif a == b and b != c or a == c and a != b or b == b and b != a:
    print('vordhaarne kolmnurk')
else:
    print('erikulgne kolmnurk')