def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params(6)
print_params(6, 7)
print_params()

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 'string2', False]
values_dict = {'a': 77, 'b': 31.7, 'c': True, }

print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'строка']

print()
print_params(*values_list_2, 42)
