from jproperties import Properties

configs = Properties()
with open('databasetest.properties', 'rb') as config_file:
    configs.load(config_file)
d = len(configs)
items_view = configs.items()
list_keys = []

for item in items_view:
    list_keys.append(item[0])
#print(list_keys)
print('Количество элементов в словаре', d)
print("Возможные варианты:")

list_value = []
for item in items_view:
    list_value.append(item[1].data)
#print(list_value)
i = 0
for item in items_view:
    print(i + 1, "элемент имеет ключ", list_keys[i])
    i += 1

while True:
    try:
        value = int(input('Введите интересующий элемент словаря '))
        a = list_value[0:][value - 1]
        b = list_keys[0:][value - 1]
        print(b,'=',a)
        break
    except ValueError:
        print("Введите цифру!")
    except IndexError:
        print("У Вас,", d, "значения! А вы вводите", value,". Попробуйте еще раз")
