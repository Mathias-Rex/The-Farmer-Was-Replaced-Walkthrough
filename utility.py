# importáljuk itt is configot
import config

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

def use_water():
    if num_items(Items.Water) > 1 and get_water() < 0.5:
        use_item(Items.Water)

# És használjuk is
def use_fertilizer():
    if config.req_fertilizer == False:
        return False
    if num_items(Items.Fertilizer) > 1:
        use_item(Items.Fertilizer)

def prepare_ground(req_ground):
    harvest_if_possible()
    if get_ground_type() != req_ground:
        till()
    use_water()