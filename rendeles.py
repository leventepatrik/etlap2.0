import kozos_eljaras
def foetel():
    ar1: int=0
    valasztott_etel=""
    kozos_eljaras.csillagok("*", 36)#32 csillag fejléc
    kerfoetelt:str=input("Kér Főételt? I/N: ")
    kozos_eljaras.csillagok("*", 36)#32 csillag fejléc
    elso_foetel:str="1. Rakottkrumpli"
    elso:int=300
    masodik_foetel:str="2. Spenotos tészta"
    masodik:int=300
    if kerfoetelt=="I" or "i":
        kozos_eljaras.rendeles_etel(f"{elso_foetel}", f"{elso}")
        kozos_eljaras.rendeles_etel(f"{masodik_foetel}", f"{masodik}")
    kozos_eljaras.csillagok("*", 36)  # 36 csillag fejléc
    foetel_be_szam=input("Melyik főételt kéri? ") #ebbe tárolom melyik fő ételt választotta számként van megadva
    ar1:int=0 #ebbe tárolom a választott lev
    if foetel_be_szam == "1":  # ha a választott leves 1 akkor az ar2 változoba a leves elso változo árát menti el
        ar1 = elso
    else:
        ar1 = masodik  # különben ha a masodik levest választotta akkor az ar2 változoba a masodik változo árát menti el

    if foetel_be_szam == "1":
        valasztott_etel = elso_foetel
    else:
        valasztott_etel= masodik_foetel

def leves():
    valasztott_etel2 =""
    ar2: int=0
    kozos_eljaras.csillagok("*", 36)#36 csillag fejléc
    kerlevest:str=input("Kér Levest? I/N: ")
    elso_leves:str="1. Franciahagyma leves"
    elso:int=300
    masodik_leves:str="2. Barackrém leves"
    masodik:int=300
    if kerlevest=="I" or "i":
        kozos_eljaras.rendeles_etel(f"{elso_leves}", f"{elso}")
        kozos_eljaras.rendeles_etel(f"{masodik_leves}", f"{masodik}")
    kozos_eljaras.csillagok("*", 36)  # 32 csillag fejléc
    leves_be=input("Melyik Levest kéri? ") #ebbe tárolom melyik fő ételt választotta számként van megadva
    ar2: int = 0 #ebbe tárolom a választott leves árát
    if leves_be == "1": #ha a választott leves 1 akkor az ar2 változoba a leves elso változo árát menti el
        ar2 = elso
    else:
        ar2 = masodik #különben ha a masodik levest választotta akkor az ar2 változoba a masodik változo árát menti el

    if leves_be == "1":
        valasztott_etel = elso_leves
    else:
        valasztott_etel = masodik_leves
