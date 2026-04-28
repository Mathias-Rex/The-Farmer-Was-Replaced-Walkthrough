import plant
import utility

def custom(custom_map):
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.smart(custom_map[y][rx])

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

# Az első kör teljesen felesleges, hiszen elég lenne csak a
# maző koordinátáival feltölteni a tömbünket először!
def pumpkin():
    pumpkin_map = []
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            pumpkin_map.insert(0, (rx, y))

    while len(pumpkin_map) > 0:
        for _ in range(len(pumpkin_map)):
            coord = pumpkin_map.pop()
            x = coord[0]
            y = coord[1]
            utility.goto(x, y)
            if get_entity_type() != Entities.Pumpkin:
                plant.pumpkin()
                pumpkin_map.insert(0, (x, y))
    harvest()