# Rakjunk be még egy kis védelmet a túllocsolás ellen!
# Sőt legyen egy okosz locsoló függvényünk ebből is

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

def prepare_ground(req_ground):
    harvest_if_possible()
    if get_ground_type() != req_ground:
        till()
    use_water()