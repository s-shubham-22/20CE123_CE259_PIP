item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda x: x**2, item_list))

print(square)

for i in item_list:
    print(list(map(lambda function:function(i), [lambda x: x+x, lambda x: x**2, lambda x: x**3, lambda x: x**4])))