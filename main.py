# Ne kapáljunk ha nem kell.
# Második lépésként pedig ne mozogjunk feleslegesen.
# Aktiváljuk a kommentelt a sorokat a kódban, és a
# goto(x, y)-t pedig töröljük, vagy kommenteljük ki.

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

while True:
    for y in range(3):
        for x in range(3):
            #rx = x
            #if y % 2 != 0:
            #   rx = 3 - x - 1
            #goto(rx, y)
            goto(x, y)
            if can_harvest():
                harvest()
            if get_pos_y() == 0:
                if get_ground_type() == Grounds.Grassland:
                    till()
                plant(Entities.Carrot)
            if get_pos_y() == 1:
                plant(Entities.Bush)
