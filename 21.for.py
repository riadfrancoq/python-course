"""
for element in range(1,21): # el ultimo valor no va incluido 
    print(element)

"""

my_list = [23, 45, 67, 89, 43 ]

for element in my_list:
    print(element)

my_tuple = ('nico', 'juli', 'santi')

for element in my_tuple:
    print(element)


product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}
for element in product:
    print(product[element])


for key, value in product.items():
    print(f"key {key} and value {value}")

people = [
    {
        'name': 'nico',
        "age": 34
    },
    
    {
        'name': 'zule',
        "age": 45
    },
    
    {
        'name': 'santi',
        "age": 4
    }

]
print(people[0]['name']) # para buscar en una array
for person in people:
    print(person['name'])

    