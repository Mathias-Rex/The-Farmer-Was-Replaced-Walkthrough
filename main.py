# De ez az ültetés nem elég okos:
#  * nem készíti elő a talajt és
#  * nem locsolja meg a növényt.
# Készítsünk egy okos ültetés függvényt!

import field
import utility
import plant


req_wood = 850
req_carrot = 500
req_hay = 800

def plant_smart(entity):
    if entity == Entities.Bush:
        plant.bush()
    if entity == Entities.Tree:
        plant.tree()
    if entity == Entities.Grass:
        plant.grass()
    if entity == Entities.Carrot:
        plant.carrot()

while True:
    custom_map = [
      [Entities.Bush, Entities.Tree, Entities.Bush, Entities.Carrot],
      [Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree],
      [Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot],
      [Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Tree]
    ]
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            utility.harvest_if_possible()
            plant_smart(custom_map[y][rx])

#    if num_items(Items.Hay) < req_hay:
#        field.grass()
#    elif num_items(Items.Wood) < req_wood:
#        field.forest()
#    else:
#        field.carrot()
