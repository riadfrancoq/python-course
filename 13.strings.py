text = "Ella sabe programar en Python"

# busca dentro de un text
"""
print('Python' in text)

if 'JS' in text:
    print('Elegiste bien!')
else:
    print('Tambien elegiste bien')
"""

size = len('amor ')

print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase()) # pasa lo que esta en minuscula a mayuscula y viseversa

print(text.startswith('Ella'))
print(text.endswith('Python'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'

print(text_2)
print(text_2.capitalize()) # Poner el primer caracter en mayuscula
print(text_2.title()) # poner el inicio de cada palabra en mayuscula
print(text_2.isdigit())
print("2".isdigit())
