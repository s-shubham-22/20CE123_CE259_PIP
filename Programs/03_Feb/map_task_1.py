fruits = ['apple', 'banana', 'cherry', 'durian', 'fig', 'grape', 'honeydew', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'peach', 'pear', 'pineapple', 'plum', 'pomegranate', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']

fruits_starting_with_a = []
fruits_ending_with_e = []

def distribute_fruits(fruit):
        if fruit[0] == 'a':
            fruits_starting_with_a.append(fruit)
        if fruit[-1] == 'e':
            fruits_ending_with_e.append(fruit)

list(map(distribute_fruits, fruits))
print(f"Fruits name starting with 'a': {fruits_starting_with_a}")
print(f"Fruits name ending with 'e': {fruits_ending_with_e}")
