import plant
import utility

def forest():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            if (rx + y) % 2 == 0:
                plant.bush()
            else:
                plant.tree()

def grass():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.grass()

def carrot():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.carrot()