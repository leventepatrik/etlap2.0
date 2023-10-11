import kozos_eljaras
import rendeles


def foetel():
    kozos_eljaras.csillagok("*", 40)#32 csillag fejléc
    kerfoetelt:str=input("Kér Főételt? I/N: ")
    kozos_eljaras.csillagok("*", 40)#32 csillag fejléc
    elso_foetel:str="1. Rakottkrumpli"
    elso:int=300
    masodik_foetel:str="2. Spenotos tészta"
    masodik:int=300
    if kerfoetelt=="I" or "i":
        kozos_eljaras.rendeles_etel(f"{elso_foetel}", f"{elso}")
        kozos_eljaras.rendeles_etel(f"{masodik_foetel}", f"{masodik}")
    kozos_eljaras.csillagok("*", 40)  # 32 csillag fejléc
    foetel_be_szam:int=input("Melyik főételt kéri? ") #ebbe tárolom melyik fő ételt választotta számként van megadva
    ar1:int=0 #ebbe tárolom a választott lev


    if foetel_be == elso_foetel:
        ar1== elso
    else:
        ar1== masodik


def leves():
    kozos_eljaras.csillagok("*", 40)#32 csillag fejléc
    kerlevest:str=input("Kér Levest? I/N: ")
    elso_leves:str="1. Franciahagyma leves"
    elso:int=300
    masodik_leves:str="2. Barackrém leves"
    masodik:int=300
    if kerlevest=="I" or "i":
        kozos_eljaras.rendeles_etel(f"{elso_leves}", f"{elso}")
        kozos_eljaras.rendeles_etel(f"{masodik_leves}", f"{masodik}")
    foetel_be:int=input("Melyik Levest kéri? ") #ebbe tárolom melyik fő ételt választotta számként van megadva
    ar2: int = 0 #ebbe tárolom a választott leves árát
    if foetel_be == elso_leves:
        ar2 == elso
    else:
        ar2 == masodik


