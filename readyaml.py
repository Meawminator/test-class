import yaml
with open('client.yaml') as fh:
    read_data = yaml.load(fh, Loader=yaml.FullLoader)
    sorted_data = yaml.dump(read_data, sort_keys=False)
d = len(read_data['client'])
print('Количество элементов в словаре', d)
print("Возможные варианты:")
i = 0
for name in read_data['client']:
    print(i + 1, "элемент имеет ключ", read_data['client'][i]["name"])
    i += 1

while True:
    try:
        value = int(input('Введите интересующий элемент словаря '))
        a = read_data['client'][0:][value - 1]
        print(a)
        break
    except ValueError:
        print("Введите цифру!")
    except IndexError:
        print("У Вас,", d, "значения! А вы вводите", value,". Попробуйте еще раз")
