# Nyissuk ki az Expandot megint!
# 4x4-es terület a jutalmunk!
# De csak 3x3-as területet művelünk meg...
# Hogyan lehet megoldani, hogy ne
# kelljen ezzel már többet foglalkozni?
# 4-et írni a 3 helyére a for ciklusba.
# vagy inkább használni a get_world_size()-t
# Ha túl sok a szalma ültessünk mást!

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
    for y in range(get_world_size()):
        for x in range(get_world_size()):
            rx = x
            if y % 2 != 0:
                rx = get_world_size() - x - 1
            goto(rx, y)
            if can_harvest():
                harvest()
            if get_pos_y() == 0 or get_pos_y() == 2:
                if get_ground_type() == Grounds.Grassland:
                    till()
                plant(Entities.Carrot)
            if get_pos_y() == 1:
                plant(Entities.Bush)
