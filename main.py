# Alakítsuk át a térképünket jobban olvashatóvá
# Tömb a tömbben, azaz 2 dimenziós tömb.

import field
import utility

req_wood = 850
req_carrot = 500
req_hay = 800

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
            plant(custom_map[y][rx])

#    if num_items(Items.Hay) < req_hay:
#        field.grass()
#    elif num_items(Items.Wood) < req_wood:
#        field.forest()
#    else:
#        field.carrot()
