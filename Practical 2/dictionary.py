# 20CE123 - Shubham Sareliya
# Github Link: https://github.com/s-shubham-22/20CE123_CE259_PIP.git

# a. Write a Python script to check whether a given key already exists in a dictionary.
my_dict = {
    1: 'Shubham',
    2: 'Deep',
    3: 'Heer'
}

print('A:')
print(f'my_dict: {my_dict}')
print(my_dict.get(1))
print('')

# b. Write a Python script to merge two Python dictionaries.
my_dict2 = {
    4: 'Kalpit',
    5: 'Minaxi',
    6: 'Sagar'
}

my_dict3 = {**my_dict, **my_dict2}
print('B:')
print(f'my_dict: {my_dict}')
print(f'my_dict2: {my_dict2}')
print(f'my_dict3: {my_dict3}')
print('')

# c. Write a Python program to sum all the items in a dictionary.
my_dict4 = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4
}
print('C: ')
print(f'my_dict4: {my_dict4}')
print(f'Sum of Values: {sum(my_dict4.values())}')
print('')

# d. Write a Python script to add a key to a dictionary.
my_dict5 = {
    0: 10,
    1: 20 
}
print('D: ')
print('Before Adding key: ')
print(f'Old Dictionary my_dict5: {my_dict5}')
my_dict5[2] = 30
print('After Adding key: ')
print(f'New Dictionary my_dict5: {my_dict5}')

# e. Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {
    1: 10,
    2: 20
}
dic2 = {
    3: 30,
    4: 40
}
dic3 = {
    5: 50,
    6: 60
}

sum_dic = {**dic1, **dic2, **dic3}

print('E: ')
print(f'dic1: {dic1}')
print(f'dic2: {dic2}')
print(f'dic3: {dic3}')
print(f'sum_dic: {sum_dic}')