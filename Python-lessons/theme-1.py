# Переменные и типы данных
# = - оператор присваивания

age = 27
# print("Мне", age, "лет")

# Нотации
# snake_case
client_name = 'Boris'
client_age = 27
# camelCase
clientName = 'Artyom'
clientAge = 17
# PascalCase
ClientName = 'Ivan'
ClientAge = 18

# Правила наименования переменных
# Только латинские символы a-zA-Z
# Цифры, но не на первой позиции
# Знак нижнего подчеркивания _
client1 = 1
client2 = 2

# Типы данных
# integer / int / целое число
my_int = 10
print(my_int, type(my_int))

# float / float / вещественное число
my_float = 10.5
print(my_float, type(my_float))

# string / str / строка
my_str_1 = 'Hello1'
my_str_2 = "Hello2"
my_str_3 = '"Hello3"'
print(my_str_1, type(my_str_1))
print(my_str_2, type(my_str_2))
print(my_str_3, type(my_str_3))

# list / list / список
my_list = ['Sasha', 20, 170.5]
print(my_list, type(my_list))
# У каждого элемента списка есть свой порядковый номер
# Нумерация элементов списка всегда начинается с 0
print(my_list[0], type(my_list[0]))
print(my_list[1], type(my_list[1]))

# tuple / tuple / кортеж
my_tuple = (19, 'hello', 8.9)
print(my_tuple, type(my_tuple))

# set / set / множество
my_set = {1, 1, 1, 1, 2, 3, 2, 3}
print(my_set, type(my_set))

# dictionary / dict / словарь
my_dict = {'age': 17, 'height': 180, 'name': 'Egor'}
print(my_dict, type(my_dict))

# boolean / bool / логический тип данных
my_bool_1 = True
my_bool_2 = False
print(my_bool_1, type(my_bool_1))