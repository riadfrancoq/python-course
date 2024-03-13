name = "Nicolas"
print(type(name))

name = 2
print(type(name))
 
name = True
print(type(name))


# Tipado Dinamico 

print("Nicolas" + "Molina")
print(10 + 20)
print("Nicolas" + "12")

age = 12
print("Mi edad es " + str(age) )
print(f"Mi edad es {age}")

age = input("Escribe tu edad ")

print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 anos sera {age}')