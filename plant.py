# itt pedig távolítsuk el a "plant_" részt
# minden függvény elől

import utility

# itt is be kell importálnunk a utility-t,
# hiszen használjuk a függvényit.
# prepare_ground függvényt utility.prepare_ground-ra
# kell mnódosítani mindnhol

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