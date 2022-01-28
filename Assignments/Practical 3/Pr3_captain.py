def captainRoom(rooms):
    room_no = list(dict.fromkeys(rooms))
    for x in room_no:
        if rooms.count(x) == 1:
            return x

k = int(input())
rooms = [int(item) for item in input().split(" ")]

print(captainRoom(rooms))