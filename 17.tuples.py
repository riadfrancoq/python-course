#tuples
# tuples cannot be modified 
nottuple = ('Apple')
print(type(nottuple))

numbers = (1,2,3,4,5)  
strings = ('nico','zule','santi','nico')

print(numbers)
print('0 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))


print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings) # tuple to list
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(type(my_tuple))