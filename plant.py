import utility

def carrot():
    if num_items(Items.Wood) < 1:
        bush() # ha fánk nincs akkor bokrot
    elif num_items(Items.Hay) < 1:
        grass() # ha szalmánk nincs akkor azt
    else:
        utility.prepare_ground(Grounds.Soil)
        plant(Entities.Carrot)

def grass():
    utility.prepare_ground(Grounds.Grassland)

def bush():
    utility.prepare_ground(Grounds.Grassland)
    plant(Entities.Bush)

def tree():
    utility.prepare_ground(Grounds.Grassland)
    plant(Entities.Tree)

def smart(entity):
    if entity == Entities.Bush:
        bush()
    if entity == Entities.Tree:
        tree()
    if entity == Entities.Grass:
        grass()
    if entity == Entities.Carrot:
        carrot()