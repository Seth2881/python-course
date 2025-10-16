def speedConv()->str :
    kph = input("Donnez une vitesse en km/h : ")
    return f"{kph} km/h = {round(float(kph)*0.621371 , 2)} mp/h"

print(speedConv())