# Nyissuk ki a:
#  * a 6x6-os farmot az Expanddal
#  * Grass-t 2x
#  * répát és
#  * speedet
#  * egy kicsit termeljünk
# hogy ki tudjuk nyitni a Sunflowert
# készítsük el a sunflower ültető függvényeket a
# plant és a field fájlban, valamint a
# smart függvényt is egészítsük ki az új sunflower()
# függvénnyel.
# Az okos teremlést is javítsuk ki a mainben 

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
        field.pumpkin()

#    custom_map = [
#      [Entities.Bush, Entities.Tree, Entities.Bush, Entities.Carrot],
#      [Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree],
#      [Entities.Bush, Entities.Carrot, Entities.Tree, Entities.Carrot],
#      [Entities.Carrot, Entities.Tree, Entities.Bush, Entities.Tree]
#    ]
#    field.custom(custom_map)

    