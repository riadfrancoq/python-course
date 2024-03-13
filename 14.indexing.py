text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999]) si no existe esa posicion le va a dar un error
size = len(text)
print(f'size => {size}')
print(text[size -1 ]) 
print(text[-1])


#slicing 

print(text[0:5])
print(text[10:16])
print(text[:10]) # si no colocamos el primer caracter va a obivar y va empezar desde el 0
print(text[5:-1])
print(text[5:]) # si lo pasamos el ultimo caracter tiene que ir al final
print(text[:])
print(text[10:16:1])
print(text[10:16:2]) # ese ultimo caracter es para saltos
print(text[::2]) # empieze desde el inicio al final y salta dos elementos