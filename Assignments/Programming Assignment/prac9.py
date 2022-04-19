class Point(object):
    pass

class Rectangle(object):
    pass

rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = 8.0
bottom_left.y = 3.0

top_right = Point()
top_right.x = 9.0
top_right.y = 6.0

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = 15.0
dy = 16.0

def move_rectangle(rectangle, dx, dy):
    print(f"The rectangle started with bottom left corner at ({rectangle.corner1.x},{rectangle.corner1.y})"
          f"\nTop right corner at ({rectangle.corner2.x},{rectangle.corner2.y})"
          f"\ndx is {dx} and dy is {dy}")
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print(f"It ended with a bottom left corner at ({rectangle.corner1.x},{rectangle.corner1.y})"
          f"\nTop right corner at ({rectangle.corner2.x},{rectangle.corner2.y})")

move_rectangle(rectangle, dx, dy)