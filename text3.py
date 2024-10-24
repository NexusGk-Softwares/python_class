#creating a simple dictionary with 5 items
fruits = {
    'apple': 1,
    'banana': 2,
    'orange': 3,
    'grape': 4,
    'kiwi': 5,
}

#accessing elements using key   
print(fruits['apple'])  # prints 1
print(fruits['banana'])  # prints 2

#updating elements
fruits['banana'] = 5
print(fruits['banana'])  # prints 5

#deleting elements
del fruits['orange']
print(fruits)  # prints {'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5}

#checking if a key exists
if 'pear' in fruits:
    print('pear is present in the dictionary')
else:
    print('pear is not present in the dictionary')

#adding new elements
fruits['pear'] = 6
print(fruits)  # prints {'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5, 'pear': 6}

#updating existing elements
fruits['pear'] = 7
print(fruits)  # prints {'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5, 'pear': 7}

#clearing all elements
fruits.clear()
print(fruits)  # prints {}

#checking if the dictionary is empty
if fruits:
    print('the dictionary is not empty')
else:
    print('the dictionary is empty')

#converting a dictionary to a list of tuples
dictionary_fruits = list(fruits.fruits())
print(dictionary_fruits)  # prints [('apple', 1), ('banana', 5), ('grape', 4), ('kiwi', 5), ('pear', 7)]

#converting a list of tuples back to a dictionary
dictionary_from_tuples = dict(dictionary_fruits)
print(dictionary_from_tuples)  # prints {'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5, 'pear': 7}

#converting a dictionary to a string
dictionary_as_string = str(fruits)
print(dictionary_as_string)  # prints "{'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5, 'pear': 7}"

#converting a string back to a dictionary
dictionary_from_string = eval(dictionary_as_string)
print(dictionary_from_string)  # prints {'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5, 'pear': 7}

#converting a dictionary to a JSON string
import json
dictionary_as_json = json.dumps(fruits)
print(dictionary_as_json)  # prints '{"apple": 1, "banana": 5, "grape": 4, "kiwi": 5, "pear": 7}'

#converting a JSON string back to a dictionary
dictionary_from_json = json.loads(dictionary_as_json)
print(dictionary_from_json)  # prints {'apple': 1, 'banana': 5, 'grape': 4, 'kiwi': 5, 'pear': 7}

