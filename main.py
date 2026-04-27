# Csináljunk egy függvényt abból, hogy egy erdőt ültetünk és
# egy másikat, hogy répát

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

def plant_forest():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            if (rx + y) % 2 == 0:
                plant_bush()
            else:
                plant_tree()

def plant_carrot_field():
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            plant_carrot()

while True:
    plant_carrot_field()
    plant_forest()