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
print("dropwhile(predicate, iterable)") # using dropwhile() to start displaying after condition is false
li = [2, 4, 5, 8, 9]
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))
print()

# filterfalse(predicate, iterable)
print("filterfalse(predicate, iterable)") # using filterfalse() to print false values
print(list(itertools.filterfalse(lambda x : x % 2 == 0, li)))
print()

# groupby(iterable, keyfunc)
print("groupby(iterable, keyfunc)")
key_pair = [('a', 1), ('a', 2), ('b', 3), ('c', 4), ('c', 5)]
for key, group in itertools.groupby(key_pair, lambda x : x[0]):
    print(f'{key}: {list(group)}')
print()

# islice(iterable, start, stop, step)
print("islice(iterable, start, stop, step)")
print(list(itertools.islice(range(10), 2, 8, 2))) # start, stop, step

# pairwise(iterable)
print("pairwise(iterable)")
print(list(itertools.pairwise('ABCDE')))
print()

# starmap(function, iterable)
print("starmap(function, iterable)")
print(list(itertools.starmap(operator.add, [(1, 2), (3, 4), (5, 6)])))
print()

# takewhile(predicate, iterable)
print("takewhile(predicate, iterable)")
print(list(itertools.takewhile(lambda x : x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print()

# tee(iterator, count)
print("tee(iterator, count)")
li = [1, 2, 3, 4, 5]
iti = iter(li)
it = itertools.tee(iti, 3)
for i in range(3):
    print(list(it[i]))
print()

# zip_longest(p, q, fillvalue=None)
print("zip_longest(p, q, fillvalue=None)")
print(list(itertools.zip_longest('ABCD', 'xy', fillvalue='-')))
print()

