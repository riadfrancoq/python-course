"""
a = 10
while a < 100:
    a += 1
    print('se ejecuto')
else:
    print('???')

counter = 0
while counter < 10:
    counter += 1
    print(counter)
else:
    print('ua')


counter  = 0 

while counter < 20:
    counter += 1
    if counter == 15: break
    print(counter)
else:
    print(' llego a 20?')
"""


counter = 0 
while counter < 20:
    counter += 1 
    if counter < 15: continue
    print(counter)