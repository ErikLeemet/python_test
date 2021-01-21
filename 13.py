text = input('Tekst: ')

if len(text) < 7 or len(text) % 2 == 0:
    print('kirjuta rohkem')
else:
    middle_index = int(len(text) / 2)
    print(text[middle_index -1] + text[middle_index] + text[middle_index+1])