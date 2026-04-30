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

def sunflower():
    sunflower_map = { 0: [] }
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.sunflower()
            sunflower_map[0].insert(0, (rx, y))

    for _ in range(len(sunflower_map[0])):
        coord = sunflower_map[0].pop()
        x = coord[0]
        y = coord[1]
        utility.goto(x, y)
        petalNr = measure()
        if petalNr not in sunflower_map:
            sunflower_map[petalNr] = []
        sunflower_map[petalNr].insert(0, (x, y))

    for petalNr in range(15, -1, -1):
        if petalNr in sunflower_map:
            for coord in sunflower_map[petalNr]:
                x = coord[0]
                y = coord[1]
                utility.goto(x, y)
                harvest()

# Tegyül el egy tömbben, az utlsó n helyet egy változóba,
# hogy honnét jöttünk, és ha ugyanoda kell mennünk, ahol
# nemrég voltunk már, akkor menjünk egy random kooordinátára.
# Nyissuk ki a random() függvényt ehhez!
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
