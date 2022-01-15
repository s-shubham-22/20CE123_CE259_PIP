# a. Write a Python program to create a tuple with different data types.
my_tuple = (1, 2.5, True, 'Shubham')
print('A: ')
print(f'my_tuple: {my_tuple}')
print('')

# b. Write a Python program to create a tuple with numbers and print one item.
my_tuple2 = (1, 2, 3, 4, 5)
print('B: ')
print(f'my_tuple2: {my_tuple2}')
print(f'my_tuple2[2]: {my_tuple2[2]}')
print('')

# c. Write a Python program to add an item in a tuple.
my_tupple3 = (1, 2, 3)
print('C: ')
print(f'Old my_tuple3: {my_tupple3}')
my_tupple3 = my_tupple3 + (4,)
print(f'New my_tuple3: {my_tupple3}')
print('')

# d. Write a Python program to convert a tuple to a string.
my_tupple4 = ('S', 'h', 'u', 'b', 'h', 'a', 'm')
strTupple = ''.join(my_tupple4)
print('D: ')
print(f'my_tupple4: {my_tupple4}')
print(f'my_tupple4 converted into string: {strTupple}')
print('')

# e. Write a Python program to find the length of a tuple.
my_tupple5 = ('a', 4, 4.6, True, 'Hello')
print('E:')
print(f'my_tupple5: {my_tupple5}')
print(f'Length of my_tupple5: {len(my_tupple5)}')
print('')
