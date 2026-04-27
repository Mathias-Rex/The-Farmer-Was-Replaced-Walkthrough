# Csináljunk egy okos fű ültető függvényt és
# egy bokor ültető függvényt is.

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

def plant_carrot():
    if num_items(Items.Wood) > 1 or num_items(Items.Hay) > 1:
        if get_ground_type() == Grounds.Grassland:
            till()
        plant(Entities.Carrot)
    else:
        plant_bush() # itt is cseréljük ki, így nem fogja talajra ültetni a bokrot

def plant_grass():
    if get_ground_type() != Grounds.Grassland:
        till() # ha talaj akkor legyen fű

def plant_bush():
    # ne ültessük a bokrot talajra
    if get_ground_type() != Grounds.Grassland:
        till()
    plant(Entities.Bush)

while True:
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            if can_harvest():
                harvest()
            if get_pos_y() == 0 or get_pos_y() == 2:
                plant_carrot()
            if get_pos_y() == 1:
                plant_bush()
