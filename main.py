# Nyissuk ki a műtrűgyűt is / Fertilizer
# és a Utilityben készítsük el a use_fetilizer
# függvényt, a use_waterhez hasonlóan!

# Nyissunk egy új fájlt config néven és minden
# req_ kezdetű változót tegyünk át oda!
# Ezentúl ez fogja szabályozni az appunk teljes
# beállítását!
# Javítsuk meg az itt használ req_ változókat
# a commentekben is

import config
import field

while True:
    custom_map = [
      [Entities.Bush, Entities.Tree, Entities.Bush, Entities.Carrot],
      [Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree],
      [Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot],
      [Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Tree]
    ]
    field.custom(custom_map)

#    if num_items(Items.Hay) < config.req_hay:
#        field.grass()
#    elif num_items(Items.Wood) < config.req_wood:
#        field.forest()
#    else:
#        field.carrot()
