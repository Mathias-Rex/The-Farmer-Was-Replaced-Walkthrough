# Tegyük megint a helyére az okos ültetést!
# Másoljuk át a plant fájlba/modulba és
# innét töröljük a plant_smart függvényt!
# Ha a plant-ban átneveztük cseréljök
# a "_"-t "."-ra a for ciklusban!

import field
import utility
import plant

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
            plant.smart(custom_map[y][rx])

#    if num_items(Items.Hay) < req_hay:
#        field.grass()
#    elif num_items(Items.Wood) < req_wood:
#        field.forest()
#    else:
#        field.carrot()
