import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

print(phonebook['Chris'])

print()
print('*****  end section 1 ********')
print()


'''


print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'
if name in phonebook:
    print(f'The phone number is', phonebook[name])
else:
    print(f'{name} is not in the phonebook')




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'
print(phonebook)



print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)



print()
print('*****  end section 4 ********')
print()





print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

#the default iteration for a dictionary are the keys
for key in phonebook:
    print(f'the key of the dictionary is {key} and the value is {phonebook[key]}')

#this will iterate through the values
for value in phonebook.values():
    print(value)

#this will iterate through both keys and values:
for item in phonebook.items():
    print(item)
#this will iterate through both keys and values (split):
for k,v in phonebook.items():
    print(f'the key of the dictionary is {k} and the value is {v}')

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris', '911')
print(phone)

phonebook.clear()
print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


phone = phonebook.pop('Chris', 'not found')
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

item = phonebook.popitem()
print(item)
print(phonebook)


print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

#alternatively in one line
phone = phonebook[random.choice(list(phonebook))]
print(phone)



print()
print('*****  end section 9 ********')
print()








