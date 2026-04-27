# Okosítsunk és nyissuk ki a Variable és a Defet is.
# A Def a Scratchben a saját blokkhoz hasonlóan egy
# kis programrészlet, amit bárhonnát meghívhatunk.
# Készítsünk egy függvényt, amivel a drónunkat
# bármelyik koordinátára elküldhetjük.

def goto(x, y):
    # Addig mozgunk, amíg el nem érjük a kívánt helyet
    while x != get_pos_x() or y != get_pos_y():
        # Vízszintes mozgás: bal vagy jobb
        if x < get_pos_x():
            move(West)   # célpont balra van tőlünk
        elif x > get_pos_x():
            move(East)   # célpont jobbra van tőlünk
        # Függőleges mozgás: fel vagy le
        if y > get_pos_y():
            move(South)  # célpont lejjebb van
        elif y < get_pos_y():
            move(North)  # célpont feljebb van

# Teszteljük
goto(0, 0)
do_a_flip()
goto(2, 2)
do_a_flip()
goto(2, 0)
do_a_flip()
goto(0, 2)
do_a_flip()

# while True:
#     for y in range(3):
#         for x in range(3):
#             if can_harvest():
#                 harvest()
#             if get_pos_y() == 0:
#                 till()
#                 plant(Entities.Carrot)
#             if get_pos_y() == 1:
#                 plant(Entities.Bush)
#             move(East)
#         move(North)