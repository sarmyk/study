my_dict = {'Vladimir': 1989, 'Igor': 1995, 'Pavel' : 2001}
print('Dictionary: ', my_dict)
print('Existing value: ', my_dict['Vladimir'])
print('Not existing value: ', my_dict.get('Anna'))
my_dict.update({'Anna': 1995, 'Alex': 1999})
a = my_dict.pop('Igor')
print(('Deleted value: ', a))
print('Modified dictionary: ', my_dict)
print()
my_set = {1, 2, 1, 3, 5, 3, 2}
print('Set: ', my_set)
my_set.update({4, 7})
my_set.discard(3)
print('Modified set: ', my_set)
