# Задача "Распаковка"
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [220, 'пример', [3, 5, 7]]
values_dict = {'a': 660, 'b': 'еще пример', 'c': [8, 9, 10]}
values_list_2 = [54.32, 'Строка']
print_params()
print_params(11)
print_params(11, 22)
print_params(11, 22, 33)
print_params(b=25)  # Вызов работает
print_params(c=[1, 2, 3])  # Вызов работает
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)  # Вызов работает