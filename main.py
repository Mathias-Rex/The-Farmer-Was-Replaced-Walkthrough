# Termeljünk répát!
# a répa ültelés előtt kell kapálni,
# és hogy ne vesszen kárba semmi, amit
# elültettünk kitörlüm a clear()-t

while True:
    for y in range(3):
        for x in range(3):
            if can_harvest():
                harvest()
            till()
            plant(Entities.Carrot)
            move(East)
        move(North)

# Miért van az, hogy hol répt, hol szalmát
# aratunk?
# - A till a füvet (Grassland) talajjá (Soil),
#   a talajd pedig fűvé alakítja.

# Miért mozog a drónunk össze-vissza?
# - Mert nem a x=0, y=0 koordinátáról
#   indultunk, de a kódunk ezt feltételezi,
#   mindig 3-at megy vízszintesen és 3-at
#   függőlegesen!