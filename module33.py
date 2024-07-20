def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(666, "Вася", False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
values_list = [43.45, "Коля", True]
values_dict = {"a": 43.45, "b": "Коля", "c": 999}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
