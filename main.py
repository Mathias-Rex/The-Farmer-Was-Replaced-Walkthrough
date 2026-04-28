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
