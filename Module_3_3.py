# Домашнее задание по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#print_params(b = 25)
#print_params(c = [1,2,3])
#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
#print_params(a = 'Stas')
#print_params(b = 1, a = 2)
print_params()

#values_list_2 = [54.32, 'Строка', False]
values_list_2 = [54.32, 'Строка']
values_dict = {'a': 13, 'b': 'Stas', 'c': [1, 2, 3]}
print_params(values_list_2, 13)
print_params(*values_list_2, 42)
print_params(**values_dict)
