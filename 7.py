year = int(input('input an year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, 'liigaasta')
else:
    print(year, 'pole liigaasta')