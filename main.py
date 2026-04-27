# Most már tényleg oda tudjuk küldeni,
# ahová csak akarjuk.

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
            goto(x, y)
            if can_harvest():
                harvest()
            if get_pos_y() == 0:
                till()
                plant(Entities.Carrot)
            if get_pos_y() == 1:

                plant(Entities.Bush)
