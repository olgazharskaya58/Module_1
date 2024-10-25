
my_dict = {'Jane': 1986, 'Dick': 1979, 'Anna': 2003, 'Olga': 1958}
print('Dist:', (my_dict))
print('Existing value: ', my_dict['Dick'])
print('Notexisting value: ', my_dict.get('Leonid'))
my_dict.update({'Elena': 1967,
                'Robert': 1959})
a = my_dict.pop('Jane')
print('Deleted value: ', (a))
print('Modified dictionary: ', my_dict)

my_set = {False, 3.2, -6, 'Сервер', -6, False, (8, 2, 3, 2)}
print('Set:', (my_set))
my_set.update({'Словарь', 3.3})
my_set.discard(False)
print('Modified set:', (my_set))
