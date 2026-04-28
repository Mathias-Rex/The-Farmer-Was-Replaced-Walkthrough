import utility


def carrot():
    if num_items(Items.Wood) < 1:
        bush() # ha fánk nincs akkor bokrot
    elif num_items(Items.Hay) < 1:
        grass() # ha szalmánk nincs akkor azt
    else:
        utility.prepare_ground(Grounds.Soil)
        plant(Entities.Carrot)
        utility.use_fertilizer()

def pumpkin():
    if num_items(Items.Carrot) < 1:
        carrot() # ha répánk ültessünk azt
    else:
        utility.prepare_ground(Grounds.Soil)
        plant(Entities.Pumpkin)
        utility.use_fertilizer()

# Másoljuk le a pumpkin függvényt és módosítsuk,
# hogy napraforgó ültetésére alkalmas legyen
def sunflower():
    if num_items(Items.Carrot) < 1:
        carrot() # ha répánk ültessünk azt
    else:
        utility.prepare_ground(Grounds.Soil)
        plant(Entities.Sunflower)
        utility.use_fertilizer()

def grass():
    utility.prepare_ground(Grounds.Grassland)

def bush():
    utility.prepare_ground(Grounds.Grassland)
    plant(Entities.Bush)

def tree():
    utility.prepare_ground(Grounds.Grassland)
    plant(Entities.Tree)

# Gondoskodjunk a smart függvényről is
def smart(entity):
    if entity == Entities.Bush:
        bush()
    if entity == Entities.Tree:
        tree()
    if entity == Entities.Grass:
        grass()
    if entity == Entities.Carrot:
        carrot()
    if entity == Entities.Pumpkin:
        pumpkin()