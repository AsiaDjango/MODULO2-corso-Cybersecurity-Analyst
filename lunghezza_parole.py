lista_A = ["cipolla", "aglio", "sedano", "carota", "patata"]

def lunghezza_parole (lista_A):
    lunghezza = []
    for parola_radom in lista_A:
        lunghezza.append(len(parola_radom))

    return lunghezza

print (f"La lunghezza delle parole scelte {lista_A} è: {lunghezza_parole (lista_A)}")
