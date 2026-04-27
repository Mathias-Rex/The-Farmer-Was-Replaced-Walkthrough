# Most már jó sok répánk van, de nincs fánk.
# Nyissuk ki a fát, és ültessünk azt.
# Készítsünk okos fa ültető függvényt.
# De a fát pepitában kell ültetnünk!!!

def goto(x, y):
    while x != get_pos_x() or y != get_pos_y():
        if x > get_pos_x():
            move(East)
        elif x < get_pos_x():
            move(West)
        if y > get_pos_y():
            move(North)
        elif y < get_pos_y():
            move(South)

def harvest_if_possible():
    if can_harvest():
        harvest()

def prepare_ground(req_ground):
    harvest_if_possible()
    if get_ground_type() != req_ground:
        till()

def plant_carrot():
    if num_items(Items.Wood) < 1:
        plant_bush() # ha fánk nincs akkor bokrot
    elif num_items(Items.Hay) < 1:
        plant_grass() # ha szalmánk nincs akkor azt
    else:
        prepare_ground(Grounds.Soil)
        plant(Entities.Carrot)

def plant_grass():
    prepare_ground(Grounds.Grassland)

def plant_bush():
    prepare_ground(Grounds.Grassland)
    plant(Entities.Bush)
    
def plant_tree():
    prepare_ground(Grounds.Grassland)
    plant(Entities.Tree)

while True:
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            if get_pos_y() == 0 or get_pos_y() == 2:
                plant_carrot()
            if get_pos_y() == 1:
                plant_bush()

# Ezt őrittük meg, mert készőbb még jó lesz!
# while True:
#     for y in range(get_world_size()):
#         for x in range(get_world_size()):
#             rx = x
#             if y % 2 != 0:
#                 rx = get_world_size() - x - 1
#             goto(rx, y)
#             harvest_if_possible()
#             if get_pos_y() == 0 or get_pos_y() == 2:
#                 plant_carrot()
#             if get_pos_y() == 1:
#                 plant_bush()
