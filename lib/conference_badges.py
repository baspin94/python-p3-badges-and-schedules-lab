def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    speakers = [(f"Hello, my name is {name}.") for name in names]
    return speakers

def assign_rooms(names):
    rooms = []
    for index, name in enumerate(names):
        room_assign = f"Hello, {name}! You'll be assigned to room {index + 1}!"
        rooms.append(room_assign)
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges: 
        print(badge)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
