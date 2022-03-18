persons = [
    {'name': 'Anna', 'age': 25, 'gender': 'female'},
    {'name': 'Lena', 'age': 12, 'gender': 'female'},
    {'name': 'Nastya', 'age': 33, 'gender': 'female'},
    {'name': 'Angelina', 'age': 30, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Anna', 'age': 40, 'gender': 'female'},
    {'name': 'Ira', 'age': 11, 'gender': 'female'},
    {'name': 'Polina', 'age': 17, 'gender': 'female'},
    {'name': 'Oksana', 'age': 18, 'gender': 'female'},
    {'name': 'Anna', 'age': 8, 'gender': 'female'},
    {'name': 'Yana', 'age': 43, 'gender': 'female'},
    {'name': 'Kira', 'age': 18, 'gender': 'female'},
    {'name': 'Nastya', 'age': 25, 'gender': 'female'},
    {'name': 'Tamara', 'age': 31, 'gender': 'female'},
    {'name': 'Rita', 'age': 39, 'gender': 'female'},
    {'name': 'Sveta', 'age': 25, 'gender': 'female'},
    {'name': 'Anna', 'age': 22, 'gender': 'female'},
    {'name': 'Nastya', 'age': 28, 'gender': 'female'},
    {'name': 'Lera', 'age': 19, 'gender': 'female'},
    {'name': 'Sara', 'age': 10, 'gender': 'female'},
    {'name': 'Alex', 'age': 44, 'gender': 'male'},
    {'name': 'Dima', 'age': 33, 'gender': 'male'},
    {'name': 'Fedor', 'age': 38, 'gender': 'male'},
    {'name': 'Nikita', 'age': 32, 'gender': 'male'},
    {'name': 'Alex', 'age': 25, 'gender': 'male'},
    {'name': 'Foma', 'age': 7, 'gender': 'male'},
    {'name': 'Evgeniy', 'age': 25, 'gender': 'male'},
    {'name': 'Alex', 'age': 12, 'gender': 'male'},
    {'name': 'Kiril', 'age': 27, 'gender': 'male'},
    {'name': 'Mihail', 'age': 30, 'gender': 'male'}
]
quantity_of_people = 0   #
quantity_of_male = 0     #
quantity_of_female = 0     #
adults = 0                   #
list_of_names = []           #
list_of_ages = []            #
most_3_common_names = []
over35yo_men_name_starts_with_F = []


quantity_of_people = len(persons)                            # Количество всех людей

for i in range(len(persons)):
    if persons[i]['gender'] == 'male':
        quantity_of_male += 1                                # Количество мужчин
    else:
        quantity_of_female += 1                               # Количество женщин

for i in range(len(persons)):                         # Количество совершеннолетних персон
    if persons[i]['age'] >= 18:
        adults += 1

for i in range(len(persons)):                         # Список всех имён (т.к. в задании не указано иное - список с повторениями)
    list_of_names.append(persons[i]['name'])

for i in range(len(persons)):                         # Отсортированный список всех возрастов без повторений
    if persons[i]['age'] in list_of_ages:
        continue
    else:
        list_of_ages.append(persons[i]['age'])
list_of_ages.sort()

dicti = {}
set_of_names = None
fmax = 0
new_list_of_names = None

set_of_names = set(list_of_names)
new_list_of_names = list(set_of_names)
new_list_of_names.sort()
print(new_list_of_names)
# for name in new_list_of_names:
#     q = list_of_names.count(name)
#     if q > fmax:
#         fmax = q
#         dicti.update({name: q})
# print(dicti)
# # for i in range(len(set_of_names)):
# #     if
#






# print(dicti)
#most_common_names
#over35yo_men_name_starts_with_F = [i for i in persons ]
