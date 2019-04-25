with open(r'C:\Users\dombovari.agnes\Downloads\iskola.txt', "r") as f:
    szoveg = f.read()
lajos=szoveg.lower()

be = ("aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz1234567890!.?-;“”(),:")
ki = ("aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz                     ")
tabla = str.maketrans(be, ki)
lajos = lajos.translate(tabla)
lajos = lajos.strip()
lista = lajos.split()
halmaz = set(lista)
gyak = list()

for szo in halmaz:
    darab = lista.count(szo)
    gyak.append((darab, szo))
    
gyak.sort()
gyak.reverse()

with open('gyakorisag.txt', "w") as g:
    for darab,szo in gyak:
        print(darab, szo, file=g)
