goods = {'name': 'Вентилятор', 'category': 'Компьютеры', 'briefly_descripton': 'Штука, которая дует',
         'producer': 'Asus', 'price': 'Бутылка пива'
         }

for k, v in goods.items():
    print(f'{k} - {v}')
# Задание №2

millionare_cities = {
    'Днепр': 1001094,
    'Киев': 2868702,
    'Харьков': 1451132,
    'Одесса': 1017022,
}

city_region_dict = {
    'Днепр': 'Днепропетровская',
    'Киев': 'Киевская',
    'Харьков': 'Харьковская',
    'Одесса': 'Одесская',
    'Донецк': 'Донецкая',
    'Львов': 'Львовская',
}
new_dict = {}
print('\n' + '-' * 50 + '\n')
millionare_cnt = 0
var = ''
for city, region in city_region_dict.items():
    if city in millionare_cities:
        var = f'{city}-{region}'
        new_dict[var] = millionare_cities[city]
        print(f'{var} ({millionare_cities[city]})')
        millionare_cnt += 1

print(f'\nQty of millionare cities = {millionare_cnt}\n')

sorted_tuples = sorted(new_dict.items(), key=lambda item: item[1])

for el in range(len(sorted_tuples)):
    print(f'{sorted_tuples[-el - 1][0]} ({sorted_tuples[-el - 1][1]})')
