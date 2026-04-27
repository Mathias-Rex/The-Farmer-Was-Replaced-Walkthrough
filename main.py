# Jó sok kódunk van, nyissuk ki az importot és rakjunk rendet!
# A jobb felső sarokban nyissuk egy új fájlt a + gombbal.
# Kattintsunk az ablak fejlécére és nevezzük át plant-re.
# Másoljunk (innen pedig töröljük ki) át mindent ide,
# ami planttel kezdődik, kivéve:
#   * plant_forest,
#   * plant_carrot_field,
#   * plant_grass_fielde fügévyeket!
# Majd írjuk be, hogy:
import plant

# és javítsjuk:
# a plant_bush-t plant.bush-ra
# a plant_tree-t plant.tree-ra
# a plant_carrot-t plant.carrot-ra
# a plant_grass-t plant.gbush-ra

# nyissunk még egy file-t, pont mint az előbb, azt nevezzük
# utility-nek és másoljuk át:
#   * goto,
#   * harvest_if_possible,
#   * prepare_ground
# függvényeket és innen töröljük ki.
# importáljuk be a utilityt is.

import utility

# és mindenhol javítsuk a függvények nevét:
# a goto immáron:
#   * utility.goto
# lesz
# javítsuk meg a plant fájlunkat is!

# Ha mindennel végeztünk és működik a kód pihenjünk!
# Ezeket a fájlokat a fejlécükön található "-" gombbal
# összes is csukhatjük, de vigyázat az "x" kitörli a fájlt is!

def plant_forest():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            if (rx + y) % 2 == 0:
                plant.bush()
            else:
                plant.tree()

def plant_grass_field():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            plant.grass()

def plant_carrot_field():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant.carrot()

while True:
    plant_carrot_field()
    plant_forest()
    plant_grass_field()