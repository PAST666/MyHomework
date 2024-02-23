from pprint import pprint
#1 задание
from data.marvel import full_dict
#2 задание
user_input_number = (input("Введите числа через пробел:")).split(" ")
result_user_input_number = list(map(lambda x: int(x) if x.isdigit() else None, user_input_number))
print(result_user_input_number)
#3 задание
dict1 = dict(filter(lambda x: x[0] in result_user_input_number, full_dict.items()))
pprint(dict1, sort_dicts=False)
#4 задание
set1 = {dict1[i]['director'] for i in dict1}
print(set1)
#5 задание
dict2 = full_dict.copy()
for key, value in dict2.items():
    value['year'] = str(value['year'])
pprint(dict2, sort_dicts=False)
#6 задание
marvel_list = [element for element in full_dict.values()]
pprint(marvel_list, sort_dicts=False)
dict3 = list(filter(lambda film: film['title'].startswith('Ч') if isinstance(film['title'], str) else False, marvel_list))
pprint(dict3, sort_dicts=False)
#7 задание
dict4 = list(filter(lambda film: film['stage'] == 'Вторая фаза' if isinstance(film['title'], str) else False, marvel_list))
pprint(dict4, sort_dicts=False)

