import inflect
p = inflect.engine()

names = []
while True:
    try:
        user = input('Name: ')
        names.append(user)
    except EOFError:
        break

list = p.join((names))
print('Adieu,', 'adieu,', 'to', list)