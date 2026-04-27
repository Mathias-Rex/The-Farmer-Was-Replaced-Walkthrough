# Termeljünk mindent!
# mivel (majdnem) tudjuk, hogy hányadik sorban
# vagy oszlopban vagyunk, ezért
# megmondhatjuk, hogy mit kell csinálnunk!

while True:
    for y in range(3):
        for x in range(3):
            if can_harvest():
                harvest()
            if y == 0:
                till()
                plant(Entities.Carrot)
            if y == 1:
                plant(Entities.Bush)
            move(East)
        move(North)

# Miért van az, hogy hol az első sorba,
# hol a másodikba kerül a répa?
# - Ez attól függ, hogy melyik sorban áll
#   a frónunk a program indításakor.
#   valójában a drón nem tudja, hol van,
#   csak azt modntuk neki, hogy 3x készíts egy sort
#   (azaz 3x arass, ültess, menj jobbra jobbra),
#   aztán menjd felfelé