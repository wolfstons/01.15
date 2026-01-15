def beolvas():
    f=open("be1.txt","r",encoding="utf-8")
    elsosor=f.readline().strip().split(" ")
    k=int(elsosor[1])
    #print(k)
    lista=f.readlines()
    f.close()
    szekvencialista=[]
    i=0
    while i<len(lista):
        sor=lista[i].strip()
        szekvencialista.append(sor[0:k])
        i+=1
    #print(szekvencialista)
    return k,szekvencialista


def szotar_eloallitas(k,szek_lista):
    szotar={}
    for i in range (0,len(szek_lista)):
        vizsgalt=szek_lista[i]
        if len(vizsgalt)==k:
            if vizsgalt in szotar:
                szotar[vizsgalt]+=1
            else:
                szotar[vizsgalt]=1
    return szotar

def maxkeres(szotar):
    maxertek=0
    maxhely=""
    for kulcs in szotar:
        print(kulcs)
        print(szotar[kulcs])
        if szotar[kulcs]>maxertek:
            maxertek=szotar[kulcs]
            maxhely=kulcs
    return maxertek,maxhely

def fajlba_kiir():
    f=open("ki2.txt","w",encoding="utf-8")
        