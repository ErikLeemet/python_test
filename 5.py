a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a < b and a < c:
    print('min a:', a)
elif b < c:
    print('min b:', b)
else:
    print('min c:', c)
