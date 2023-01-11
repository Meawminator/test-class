import yaml
with open('client.yaml') as fh:
    read_data = yaml.load(fh, Loader=yaml.FullLoader)
    sorted_data = yaml.dump(read_data, sort_keys=False)
d = len(read_data['client'])
print('Количество элементов в словаре', d)
print("Возможные варианты:")
i = 0
for name in read_data['client']:
    print(i + 1, "элемент имеет значение", read_data['client'][i]["name"])
    i += 1
b = input('Выберете интересующий элемент словаря: ')
a = read_data['client'][0:][int(b)-1]

print(a)

#print(read_data.get('client')[])

#print(read_data.get('name', 'Kamal Hossain'))