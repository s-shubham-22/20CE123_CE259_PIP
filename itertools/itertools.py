# Github Repo: 
# https://github.com/s-shubham-22/20CE123_CE259_PIP
# References: 
# https://docs.python.org/3/library/itertools.html
# https://www.geeksforgeeks.org/python-itertools/


import itertools

# count(start, step)
print("count(start, step)")
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end =" ")

# cycle(p)
print()
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ")
        count += 1

# repeat(val, num)
print (list(itertools.repeat(25, 4)))


