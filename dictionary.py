person = {
    'name' : 'chocho',
    'age' :24
}

person['hair_color'] = 'black'

if 'name' in person:
    print('working')


person_key = list(person.keys())
print(person_key)

person_values = list(person.values())
print(person_values)

# print('nothing' in person)
# print('name' in person)

# print(person)
# print(person['name'])
# print(person['age'])