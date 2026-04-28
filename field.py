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

# Hozzunk létre egy Listát, amibe majd elmentjük azokat a
# koordinátákat, amiket ellenőriznünk kell.
# Nyissuk ki a print() függvényt is!
def pumpkin():
    pumpkin_map = []
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.pumpkin()
            pumpkin_map.insert(0, (rx, y))

    # ebben a második körben pedig ellenőrizzük le mi van elültetve
    for _ in range(len(pumpkin_map)):
        coord = pumpkin_map.pop()
        utility.goto(coord[0], coord[1])
        print(get_entity_type())