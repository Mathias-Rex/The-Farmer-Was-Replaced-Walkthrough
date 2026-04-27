# Nyissuk ki a most a Bush-t is.
# Cseréljünk kalapot és
# ültessünk és arassunk bokrot.
# Bokor sokkal lasabbaan nő, mint a fű, 
# ezért rendezzük át a kódot kicsit:
# ültetlés után hagyjuk nőni a bokrot és
# menjünk egyet északra.
# Még így is előfordul néha, hogy a
# drónunk túl gyors...    

change_hat(Hats.Green_Hat)
while True:
    plant(Entities.Bush)
    move(North)
    if can_harvest():
        harvest()
