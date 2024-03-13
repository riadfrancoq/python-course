numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

b = 2
tasks = ['make a dishes', 'play videogames ']
print(tasks)

types = [1, True, 'Hola']
print(types)


print(numbers[::2])

text = 'Hola'
# text[0] = 'W'  No es posible, porque las cadenas de text no se pueden mutar de esta manera

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3]) # es la cantidad de valores que queremos cojer de la array

print(True in types)
print('Hola' in types)