import json
from data.cities import cities_list
cities_set = {city['name'].title() for city in cities_list}
list_cities_set = list(cities_set)
# with open('newset.json', 'w', encoding='utf-8') as file:
#     json.dump(list_cities_set, file, ensure_ascii=False, indent=4)
with open('newset.json', 'r', encoding='utf-8') as file:
    python_object = set(json.load(file))
print(python_object)