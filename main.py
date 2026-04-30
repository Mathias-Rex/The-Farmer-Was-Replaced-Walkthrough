# emeljük a tök limitünket 3000-re, hogy
# kinyithassuka a Polyculturet
# ha kinyitottuk, akkor a filedben készítsük el a
# polyculture függvényt, és a else ágban használjuk is.

import config
import field

while True:
    if num_items(Items.Hay) < config.req_hay:
        field.grass()
    elif num_items(Items.Wood) < config.req_wood:
        field.forest()
    elif num_items(Items.Carrot) < config.req_carrot:
        field.carrot()
    elif num_items(Items.Pumpkin) < config.req_pumpkin:
        field.pumpkin()
    elif num_items(Items.Power) < config.req_power:
        field.sunflower()
    else:
        field.polyculture()

#    custom_map = [
#      [Entities.Bush, Entities.Tree, Entities.Bush, Entities.Carrot],
#      [Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree],
#      [Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot],
#      [Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Tree]
#    ]
#    field.custom(custom_map)

    