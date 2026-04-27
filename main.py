# Nyissuk ki a Water-t megint, hogy többet tudjunk
# locsolni. Ahhoz hogy még többet tudjunk locsolni
# harmadszor is ki kellene nyitnunk, de ahhoz
# 800 fa kell!
# Okosítsuk a rendszert! Készítsünk limiteket és
# döntsön a drón, mit termelünk!
# És hogy gyorsabban meglegyen előtte nyissuk ki a fát is újra
# Ha megvan a 800 fa nyissuk ki a vizet!

import field

req_wood = 850
req_carrot = 500
req_hay = 800

while True:
    if num_items(Items.Hay) < req_hay:
        field.grass()
    elif num_items(Items.Wood) < req_wood:
        field.forest()
    else:
        field.carrot()
