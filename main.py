import personbil
import lastbil

looping = True

#Inititierar object
opel_gron=personbil.Personbil("opel", "gron", 1)
BMW_vit=personbil.Personbil("opel", "vit", 2)

lada_red=lastbil.Lastbil("lada", "red", 3)
lada_rost=lastbil.Lastbil("lada", "rost", 4)

Personbils_lista = [opel_gron, BMW_vit]
Lastbils_lista = [lada_red, lada_rost]


def print_fordonslista(fordonslista):
    for ettfordon in fordonslista:
        ettfordon.print_fordon()

while looping:

    print("---------------------------------------")
    print("\nKlasser och arv av fordon \n ")


    val_fordon = input("Vilken fordonstyp vill du lista? 1[Lastbil] 2[Personbil]: ")
    if (val_fordon == "1"):
        print("\n Lastbilar")
        print("------------------------------------")
        print_fordonslista(Lastbils_lista)
    
    elif (val_fordon == "2"):
        print("\n Personbilar")
        print("-----------------------------------")
        print_fordonslista(Personbils_lista)

    else:
        print("\n ogiltig inmatning! \n")


    go = input("\n Vill ni lista fordonen igen? j/n ")

    if (go == "n"):
        break
    elif (go == "j"):
        continue
    else:
        print("du kan bara svar med j eller n. Programet avbryts")
        break
