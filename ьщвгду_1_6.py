my_dict = {'Alfred': 1975, 'Sister': 2004, 'Bovaritto': 1239}
print(my_dict)
print(my_dict['Sister'])
print(my_dict.get('Fedor'))
my_dict.update({'Igor': 1994, 'Stef': 1989})
print(my_dict)
n= my_dict.pop('Bovaritto')
print(my_dict)
print(n)
#
my_set = {6, 3, 'fddbg', 456, 3, True, 'sofia', 6.3, 6, 1, 'sofia'}
print(my_set)
my_set.add(342)
my_set.add((13,4,78,26))
my_set.discard(6)
print(my_set)