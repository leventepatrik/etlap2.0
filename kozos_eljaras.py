
#Levente rendelés összesités
#főcim eljaras1
def focim(jel, db):
    print(jel * db)
def szoveg_kiiaras(jel, szoveg, jel2):
    print(f"{jel} {szoveg:^32} {jel2}")

#Ételek eljaras2
def szoveg_kiiras(jel,szoveg,jel2):
    print(f"{jel} {szoveg:^28}{jel2}")

# gergő rendeléshez
# csillag32 eljara3
def csillagok(jel, db):
        print(jel * db)
def rendeles_etel(szoveg, szam):
     print(f"{szoveg:<12} {szam:>13}")

def foetelek(szöveg, db):
    print()












#ETLAP.PY fájlhoz
#a főcimek(étlap, főétel, levesek) felső keretje(eljaras1)
def focim(jel, db):
    print(jel * db)

#a főcimeknek a szöveg része(eljaras2)
def szoveg_kiiaras(jel, szoveg, jel2):
    print(f"{jel} {szoveg:^28} {jel2}")

