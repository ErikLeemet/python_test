name = input('Nimi: ')
print('tere ' + name.capitalize() + '!')

location = input('Elukoht: ')
if 'saaremaa' in location.lower():
        print('lahe!')

age = int(input('Vanus: '))

if age < 18:
    print('ei tohi autot juhtida')
elif age > 18:
    print('mis auto sul on')
else:
    print('oh oled 18')
