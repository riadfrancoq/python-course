my_dict  = { }

print(type(my_dict))

my_dict = {
    "avion": "bla bla bla",
    "name": "Nicolas",
    "last_name": "Molina Monroy",
    "age": 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name']) # si no encuntra la llave retorna un error
print(my_dict.get('unvalor')) # si no encuntra la llave retorna none

print('avion' in my_dict) # busca si existe la llave en el diccionario 
print('bla' in my_dict)
