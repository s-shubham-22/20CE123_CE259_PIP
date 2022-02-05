higher_order = lambda x, y: x**y

print(higher_order(2, 3))
print(higher_order(2, 4))
print(higher_order(2, 5))

def square(num):
    return num**2

def cube(num):
    return num**3

def higher_order_2(function, value):
    total = function(value)
    return total

print(higher_order_2(square, 2))
print(higher_order_2(cube, 2))