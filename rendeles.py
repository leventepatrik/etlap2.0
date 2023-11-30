import kozos_eljaras

def foetel(jel, etlap_meret, etel_lista, etel_ar, rendeles_lista):
    kozos_eljaras.csillagok(jel, etlap_meret)
    kerfoetelt: str = input("Kér Főételt? I/N: ")
    kozos_eljaras.csillagok(jel, etlap_meret)
    elso_foetel=etel_lista[0]
    elso_foetel_ar=etel_ar[0]
    masodik_foetel=etel_lista[1]
    masodik_foetel_ar=etel_ar[1]
    if kerfoetelt == "I" or "i":
        kozos_eljaras.rendeles_etel(f"{elso_foetel}", f"{elso_foetel_ar}Ft")
        kozos_eljaras.rendeles_etel(f"{masodik_foetel}", f"{masodik_foetel_ar}Ft")
    rendeles_szama:int= int(input("Melyik főételt kéri? "))
    rendeles_lista.append(rendeles_szama)


def leves(jel, etlap_meret, etel_lista, etel_ar, rendeles_lista):
    kozos_eljaras.csillagok(jel, etlap_meret)
    kerlevest: str = input("Kér levest? I/N: ")
    kozos_eljaras.csillagok(jel, etlap_meret)
    elso_leves=etel_lista[2]
    elso_leves_ar=etel_ar[2]
    masodik_leves=etel_lista[3]
    masodik_leves_ar=etel_ar[3]
    if kerlevest == "I" or "i":
        kozos_eljaras.rendeles_etel(f"{elso_leves}", f"{elso_leves_ar}Ft")
        kozos_eljaras.rendeles_etel(f"{masodik_leves}", f"{masodik_leves_ar}Ft")
    rendeles_szama:int= int(input("Melyik levest kéri? "))
    rendeles_lista.append(rendeles_szama)