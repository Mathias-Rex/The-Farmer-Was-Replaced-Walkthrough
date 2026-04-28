# Nyissuk ki a műtrűgyűt is / Fertilizer
# és a Utilityben készítsük el a use_fetilizer
# függvényt, a use_waterhez hasonlóan!

import field

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
    field.custom(custom_map)

#    if num_items(Items.Hay) < req_hay:
#        field.grass()
#    elif num_items(Items.Wood) < req_wood:
#        field.forest()
#    else:
#        field.carrot()
