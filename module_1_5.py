immutable_var = (1, 'string', True)
print('Immutable tuple: ', immutable_var)
#immutable_var [0] = 3   объект находится в кортеже, но не в списке с квадратными скобками, которые можно изменять
#print(immutable_var)
mutable_list = ([2, 'Hello', False])
mutable_list.append(1)
print('Mutable list: ', mutable_list)