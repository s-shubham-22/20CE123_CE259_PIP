from turtle import circle


circle_area = [23.145, 25.894, 63.857, 42.857, 12.567, 18.857, 23.145, 25.894, 63.857, 42.857, 12.567, 18.857]

a = int(input("Enter the lower bound of the list: "))
b = int(input("Enter the upper bound of the list: "))
c = int(input("Enter the number of decimal places: "))

def round_off(x):
    return round(x, c)

print(list(map(round_off, circle_area[a:b])))

