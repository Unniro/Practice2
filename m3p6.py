# Задача "Раз, два, три, четыре, пять .... Это не всё?"
def calculate_structure_sum(args):
    summa = 0
    for i in args:
        if isinstance(i, str) == True:
            summa = len(i)
            return summa + calculate_structure_sum(i - 1)
        elif isinstance(i, int) == True:
            summa += i
            return summa + calculate_structure_sum(i - 1)
        elif isinstance(i, list) == True:
            summa = sum(i)
            return summa + calculate_structure_sum(i - 1)


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
