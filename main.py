# Nyissuk ki az Operators és a Senses is.
# Máris tudjuk, hogy a drónunk.

while True:
    for y in range(3):
        for x in range(3):
            if can_harvest():
                harvest()
            if get_pos_y() == 0:
                till()
                plant(Entities.Carrot)
            if get_pos_y() == 1:
                plant(Entities.Bush)
            move(East)
        move(North)