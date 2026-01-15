"""1. feladat hogy olvasd be a be 1 txt tartalmát
    figyelj arrra gogy az elsö sor fontos ! k változó értékét innen kell ki szedni
    szekvencia_lista- ide kerülnek a tisztított adatokSTRIP()

    2. feladat dictinoary-ban fegunk tárolni 
"""
"""
végig megyünk a listán és megnézzük minden elemnél hogy szerepel e már a szótárban
 ha szerepel akkor megnöveljük az értékét a szótárban
"""


"""
FELTÉTELEZEM A 
maxertek=0
maxhely=""
végig megyek a szótáron "for kulcs in szotar:"
megnézem hogy melyik a legnagyobb értéket
nagyobb e mint az eddigi max érték
ha nagyobb, akkor eltárolom a mex erteket és maxhelyet

"""

import fugvenyek

k,szek_lista=fugvenyek.beolvas()
szotar=fugvenyek.szotar_eloallitas(k,szek_lista)
maxertek,maxhely=fugvenyek.maxkeres(szotar)

