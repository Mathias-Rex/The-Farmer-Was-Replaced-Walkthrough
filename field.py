# Itt nagyon sokszorr írjuk le ugyanazt, próbáljunk spórolni!
# Minden futás elején generáljuk le a snakepath útvonalat.
# És azt használjuk mindenfelé.

import plant
import utility

_snake_path = []
_snake_path_ready = False

def get_snake_path():
    global _snake_path
    global _snake_path_ready
    if _snake_path_ready == False:
        size = get_world_size()
        for y in range(size):
            for x in range(size):
                rx = x
                if y % 2 != 0:
                    rx = size - x - 1
                _snake_path.append((rx, y))
        _snake_path_ready = True

    snake_path = []
    for coord in _snake_path:
        snake_path.insert(len(snake_path), coord)
    return snake_path

def custom(custom_map):
    for (x, y) in get_snake_path():
        utility.goto(x, y)
        plant.smart(custom_map[y][x])

def forest():
    for (x, y) in get_snake_path():
        utility.goto(x, y)
        if (x + y) % 2 == 0:
            plant.bush()
        else:
            plant.tree()

def grass():
    for (x, y) in get_snake_path():
        utility.goto(x, y)
        plant.grass()

def carrot():
    for (x, y) in get_snake_path():
        utility.goto(x, y)
        plant.carrot()

def pumpkin():
    pumpkin_map = get_snake_path()

    while len(pumpkin_map) > 0:
        for _ in range(len(pumpkin_map)):
            coord = pumpkin_map[0]
            pumpkin_map.pop(0)
            x = coord[0]
            y = coord[1]
            utility.goto(x, y)
            if get_entity_type() != Entities.Pumpkin:
                plant.pumpkin()
                pumpkin_map.insert(len(pumpkin_map), (x, y))
            elif can_harvest() == False:
                pumpkin_map.insert(len(pumpkin_map), (x, y))
    harvest()

def sunflower():
    sunflower_map = { 0: get_snake_path() }

    for (x, y) in sunflower_map[0]:
        utility.goto(x, y)
        plant.sunflower()

    for _ in range(len(sunflower_map[0])):
        (x, y) = sunflower_map[0].pop(0)
        utility.goto(x, y)
        petalNr = measure()
        if petalNr not in sunflower_map:
            sunflower_map[petalNr] = []
        sunflower_map[petalNr].insert(0, (x, y))

    for petalNr in range(15, -1, -1):
        if petalNr in sunflower_map:
            for (x, y) in sunflower_map[petalNr]:
                utility.goto(x, y)
                harvest()

def polyculture():
    plant.smart(Entities.Carrot)
    recent_targets = []
    history_size = 6

    while True:
        companion_data = get_companion()
        if companion_data == None:
          plant.smart(Entities.Carrot)
          continue

        plant_type, (x, y) = companion_data

        is_repeat = False
        for (rx, ry) in recent_targets:
            if rx == x and ry == y:
                is_repeat = True
                break

        if is_repeat:
            tx = random() * get_world_size() // 1
            ty = random() * get_world_size() // 1
            utility.goto(tx, ty)
        else:
            recent_targets.insert(0, (x, y))
            if len(recent_targets) > history_size:
                recent_targets.pop()
            utility.goto(x, y)
            plant.smart(plant_type)
