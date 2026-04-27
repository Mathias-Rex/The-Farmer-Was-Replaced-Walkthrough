# Nyissuk ki a Expandot, és a kapunk egy 1x3-as mezőt.
# A kalapcserét pedig vegyük ki a while-ból, nem kell
# mindig kalapot cserélni

change_hat(Hats.Gray_Hat)
while True:
    if can_harvest():
        harvest()
        move(North)