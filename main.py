
import etlap

etlap_meret: int = 36

etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", "Étlap", "*", etlap_meret)

etlap.kiiras2("*", etlap_meret)

etlap.szöveg2("*", "Főétel", "*", etlap_meret)

etlap.kiiras3("*", etlap_meret)

etlap.kis_szöveg("*", "Rakott krumpli:", "300Ft", "*", etlap_meret)

etlap.kis_szöveg2("*", "Spenótos tészta:", "300Ft", "*", etlap_meret)

etlap.kiiras4("*", etlap_meret)

etlap.szöveg3("*", "Levesek", "*", etlap_meret)

etlap.kiiras5("*", etlap_meret)

etlap.kis_szöveg3("*", "Franciahagymaleves:", "300Ft", "*", etlap_meret)

etlap.kis_szöveg4("*", ":", "300Ft", "*", etlap_meret)






import rendeles
rendeles.foetel()
rendeles.leves()


import rendelesosszegzes
rendelesosszegzes.szamla("Barackrémleves",300,"Francia hagymaleves",300)
import kozos_eljaras

kozos_eljaras.focim("*", 36)
kozos_eljaras.szoveg_kiiaras("*", "Rendelés", "*")
kozos_eljaras.focim("*", 36)

kozos_eljaras.foetelek(f"", "300Ft")
kozos_eljaras.foetelek("Rakot Krumpli", "300Ft")

kozos_eljaras.focim("*", 36)
rendelesosszegzes.szoveg_kiiras("*","Köszönjük hogy a vendégünk volt","*")
kozos_eljaras.focim("*", 36)



