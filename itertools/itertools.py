# Github Repo: 
# https://github.com/s-shubham-22/20CE123_CE259_PIP
# References: 
# https://docs.python.org/3/library/itertools.html
# https://www.geeksforgeeks.org/python-itertools/


from bz2 import compress
import itertools
import operator

# count(start, step)
print("count(start, step)")
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end =" ")
print()

# cycle(p)
print("\ncycle(p)")
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ")
        count += 1
print()

# repeat(val, num)
print("\nrepeat(val, num)")
print (list(itertools.repeat(25, 4)))
print()

# accumulate(list, func)
print("accumulate(list, func)")
li = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(li, lambda x, y: x * y)))
print()

# chain(list1, list2)
print("chain(list1, list2)")
print(list(itertools.chain('ABC', 'DEF')))
print()

# chain.from_iterable(list_of_lists)
# list_of_lists = ['ABC', 'DEF']
print("chain.from_iterable(list_of_lists)")
list_of_lists = ['ABC', 'DEF']
print(list(itertools.chain.from_iterable(list_of_lists)))
print()

# compress(data, selectors)
print("compress(data, selectors)")
data = [1, 2, 3, 4, 5]
selectors = [True, False, True, True, False]
print(list(itertools.compress(data, selectors)))
print()

# dropwhile(predicate, iterable)
print("dropwhile(predicate, iterable)")

