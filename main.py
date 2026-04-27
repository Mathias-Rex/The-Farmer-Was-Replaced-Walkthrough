# Gyűjtsünk 20 fát, majd az Expandot újra.
# 3x3-as mező a jutalmunk + a for loop.
# A for loopot tudjuk hasonlítani a Scratch
# ismételd blokkjához, cset iss azt is megkapjuk,
# hogy éppen hányadik ismétlésnél tartunk!
# Fontos megértetni a gyerekekkel, hogy 0-ról
# indul a számolás!
# Kaptunk egy clear függvényt is, amit ha
# meghívunk a programunk elején "tiszta lappal"
# indulunk!
# Először while loop nélkül mutassuk mag a
# gyerekeknek, majd az egészet tegyük while-ba.
# Itt ki is térhetünk rá, hogy a teli nyíl futtatja
# a programot, az üres nyil pedig csak egy sort futtat,
# aztán megáll.

clear()
for y in range(3):
    for x in range(3):
        plant(Entities.Bush)
        move(East)
        if can_harvest():
            harvest()
    move(North)
    
# Töröld a felső kódot, hogy ez futhasson.
    
clear()
while True:
for y in range(3):
    for x in range(3):
        plant(Entities.Bush)
        move(East)
        if can_harvest():
            harvest()
    move(North)