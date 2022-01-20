# 20CE123 - Shubham Sareliya
# Github Link: https://github.com/s-shubham-22/20CE123_CE259_PIP.git

# a. Write a Python program to add member(s) in a set and clear a set
my_set = {'car', 'dog', 'bike', 'rain'}
print('A: ')
print(f'Previous my_set: {my_set}')
my_set.add('cat')
print(f'Updated my_set(added cat): {my_set}')
my_set.remove('bike')
print(f'Updated my_set(removed bike): {my_set}')
print('')

# b. Write a Python program to remove an item from a set if it is present in the set.
my_set2 = {10, 20, 30, 40, 20}
print('B:')
print(f'Old my_set2: {my_set2}')
my_set2.discard(25)
print(f'New my_set2(After using Discard Method for 25): {my_set2}')
print('')

# c. Write a Python program to create an intersection, Union, difference of sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print('C: ')
print(f'Intersection of set1 with set2: {set1.intersection(set2)}')
print(f'Union of set1 with set2: {set1.union(set2)}')
print(f'Difference of set1 with set2: {set1.difference(set2)}')
print('')

# d. Write a Python program to find maximum and the minimum value in a set.
set3 = {1, 2, 5, 3, 6, 4}
print('D:')
print(f'Maximum of set3: {max(set3)}')
print(f'Minimum of set3: {min(set3)}')
print('')

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
def most_frequent(setx):
    return max(set(setx), key = setx.count)

setx = [2, 1, 2, 1, 2, 2, 1]
print('E:')
print(f'stex: {setx}')
print(f'Most Frequent element in setx: {most_frequent(setx)}')
print('')