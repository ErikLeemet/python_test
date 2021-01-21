fruits = ['bananna', 'apple', 'pair']
print(fruits[0])
fruits.append('ploom')
print(fruits[-1])
print(fruits[len(fruits)-1])
fruits[-4] = ''
print(fruits)
if 'pirn' in fruits:
    print('pirn on listis')

print(len(fruits))
fruits.remove('pair')
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)