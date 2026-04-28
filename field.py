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

# Mindig a legnagyobb szirom sázmú virág aratásával
# kell kezdeni, hogy a legtöbb powert kapjuk
def sunflower():
    sunflower_map = { 0: [] }
    # első körben ész nélkül ültetünk ée eltesszük a 0-ás sziromszámba
    # az össezs koordinátát, hiszen azt nem tudjuk, hogy mennyi a lesz
    # a szirom szám még
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.sunflower()
            sunflower_map[0].insert(0, (rx, y))

    # a második körben leszkenneljük a sziromszámokat és minden koordinátát
    # a megfelelő szirom szám kulcs aláhelyezzük, így nem egy térképünk lesz,
    # hanem 15 darab térképen megyünk majd végig.
    for _ in range(len(sunflower_map[0])):
        coord = sunflower_map[0].pop()
        x = coord[0]
        y = coord[1]
        utility.goto(x, y)
        petalNr = measure()
        if petalNr not in sunflower_map:
            sunflower_map[petalNr] = []
        sunflower_map[petalNr].insert(0, (x,y))

    # learatjuk az előállított térképek szerint a legnagyobb sziromszámtól
    # haladva a legkisebb sziromszámig.
    for petalNr in range(15, -1, -1):
        if petalNr in sunflower_map:
            for coord in sunflower_map[petalNr]:
                x = coord[0]
                y = coord[1]
                utility.goto(x, y)
                harvest()


