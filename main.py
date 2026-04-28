# Nyissuk ki a Lists-et is és a fieldekben
# hozzunk létre egy új mező ültető függvényt

import field
import utility

req_wood = 850
req_carrot = 500
req_hay = 800

while True:
    custom_map = [Entities.Bush, Entities.Tree, Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Tree]
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            utility.goto(rx, y)
            plant(custom_map[(rx + y * 4) % len(custom_map)])

#    if num_items(Items.Hay) < req_hay:
#        field.grass()
#    elif num_items(Items.Wood) < req_wood:
#        field.forest()
#    else:
#        field.carrot()
