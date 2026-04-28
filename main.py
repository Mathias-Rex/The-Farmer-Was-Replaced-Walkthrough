# Javítsuk a tök ültetést a field-ben

import config
import field

# állítsuk vissza az okos termelési rendszer
while True:
    if num_items(Items.Hay) < config.req_hay:
        field.grass()
    elif num_items(Items.Wood) < config.req_wood:
        field.forest()
    elif num_items(Entities.Carrot) < config.req_carrot:
        field.carrot()
    elif num_items(Entities.Pumpkin) < config.req_pumpkin:
        field.pumpkin()
    else:
        field.pumpkin()

#    custom_map = [
#      [Entities.Bush, Entities.Tree, Entities.Bush, Entities.Carrot],
#      [Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree],
#      [Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot],
#      [Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Tree]
#    ]
#    field.custom(custom_map)

    