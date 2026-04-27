# A túllocsolás ellen rakjunk be még egy kis védelemt
# a utilityben

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
