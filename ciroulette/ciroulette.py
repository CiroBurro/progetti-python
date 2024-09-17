import random, time

credito = 100
numeri = range(0, 37)

def pari(numero):
    return numero % 2 == 0 and numero != 0
def dispari(numero):
    return numero % 2 != 0

num_pari = list(filter(pari, numeri))
num_dispari = list(filter(dispari, numeri))
primi_12 = range(1, 13)
secondi_12 = range(13, 25)
terzi_12 = range(25, 37)
prima_meta = range(1, 19)
seconda_meta = range(19, 37)
num_rossi = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
num_neri = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

terzine = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27],
    [28, 29, 30],
    [31, 32, 33],
    [34, 35, 36]
]

terzina_1 = terzine[0]
terzina_2 = terzine[1]
terzina_3 = terzine[2]
terzina_4 = terzine[3]
terzina_5 = terzine[4]
terzina_6 = terzine[5]
terzina_7 = terzine[6]
terzina_8 = terzine[7]
terzina_9 = terzine[8]
terzina_10 = terzine[9]
terzina_11 = terzine[10]
terzina_12 = terzine[11]

prima_riga = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
seconda_riga = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
terza_riga = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]


def scommessa():
    global credito
    while True:
        try:
            scommessa = int(input("Il tuo credito è di " + str(credito) + "€. Quanto vuoi scommettere? €"))
            if scommessa > credito:
                print("La tua scommessa è troppo alta. Riprova.")
            else:
                credito -= scommessa
                scelta = input("Cosa vuoi scommettere? \n 1. numero singolo \n 2. colore \n 3. pari/dispari \n 4. prima/seconda meta \n 5. prima/seconda/terza riga \n 6. terzina \n scelta: ")
                if scelta == "1":
                    while True:
                        try:
                            numero = int(input("Scegli un numero tra 0 e 36: "))
                            if numero in numeri:
                                puntata = int(numero)
                                print(f"Hai scommesso {scommessa}€ su un numero singolo: {puntata}")
                                break
                        except ValueError:
                            print("Inserisci un numero valido.")
                elif scelta == "2":
                    while True:
                        try:
                            colore = input("Scegli un colore (rosso/nero): ")
                            if colore in ["rosso", "nero"]:
                                puntata = colore
                                print(f"Hai scommesso {scommessa}€ su un colore: {puntata}")
                                break
                        except ValueError:
                            print("Inserisci un colore valido.")
                elif scelta == "3":
                    while True:
                        try:
                            pari_dispari = input("Scegli pari o dispari (pari/dispari): ")
                            if pari_dispari in ["pari", "dispari"]:
                                puntata = pari_dispari
                                print(f"Hai scommesso {scommessa}€ su pari/dispari: {puntata}")
                                break
                        except ValueError:
                            print("Inserisci pari o dispari.")
                elif scelta == "4":
                    while True:
                        try:
                            prima_seconda_meta = input("Scegli prima o seconda meta (prima/seconda): ")
                            if prima_seconda_meta in ["prima", "seconda"]:
                                puntata = prima_seconda_meta
                                print(f"Hai scommesso {scommessa}€ su prima/seconda meta: {puntata}")
                                break
                        except ValueError:
                            print("Inserisci prima o seconda meta.")
                elif scelta == "5":
                    while True:
                        try:
                            prima_seconda_terza_riga = input("Scegli prima, seconda o terza riga (prima/seconda/terza): ")
                            if prima_seconda_terza_riga in ["prima", "seconda", "terza"]:
                                puntata = prima_seconda_terza_riga
                                print(f"Hai scommesso {scommessa}€ su prima/seconda/terza riga: {puntata}")
                                break
                        except ValueError:
                            print("Inserisci prima, seconda o terza riga.")
                elif scelta == "6":
                    while True:
                        try:
                            terzina = input("Scegli una terzina (1-2-3, 4-5-6, 7-8-9, 10-11-12, 13-14-15, 16-17-18, 19-20-21, 22-23-24, 25-26-27, 28-29-30, 31-32-33, 34-35-36): ")
                            if terzina in ["1-2-3", "4-5-6", "7-8-9", "10-11-12", "13-14-15", "16-17-18", "19-20-21", "22-23-24", "25-26-27", "28-29-30", "31-32-33", "34-35-36"]:
                                puntata = terzina
                                print(f"Hai scommesso {scommessa}€ su una terzina: {puntata}")
                                break 
                        except ValueError:
                            print("Inserisci una terzina valida.")
                else:
                    print("Scelta non valida.")
                
                break
        except ValueError:
            print("Inserisci un numero valido.")
    return scommessa, puntata, scelta

def animazione_ruota(numero_uscito):
    print("La ruota inizia a girare...")
    time.sleep(1.5)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("0!")
    time.sleep(1.5)
    print(f"Il numero uscito è {numero_uscito}")
def ruota():
    numero_uscito = random.choice(numeri)
    return numero_uscito

def vincita(scommessa, puntata, scelta, numero_uscito):
    global credito
    if scelta == "1":
        if puntata == numero_uscito:
            print("Hai vinto!")
            credito += scommessa * 35
            return credito
        else:
            print("Hai perso!")
            return credito
    elif scelta == "2":
        if puntata == "rosso" and numero_uscito in num_rossi:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        elif puntata == "nero" and numero_uscito in num_neri:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        else:
            print("Hai perso!")
            return credito
    elif scelta == "3":
        if puntata == "pari" and numero_uscito in num_pari:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        elif puntata == "dispari" and numero_uscito in num_dispari:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        else:
            print("Hai perso!")
            return credito
    elif scelta == "4":
        if puntata == "prima" and numero_uscito in prima_meta:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        elif puntata == "seconda" and numero_uscito in seconda_meta:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        else:
            print("Hai perso!")
            return credito
    elif scelta == "5":
        if puntata == "prima" and numero_uscito in prima_riga:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        elif puntata == "seconda" and numero_uscito in seconda_riga:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        elif puntata == "terza" and numero_uscito in terza_riga:
            print("Hai vinto!")
            credito += scommessa * 2
            return credito
        else:
            print("Hai perso!")
            return credito
    elif scelta == "6":
        if puntata == "1-2-3" and numero_uscito in terzina_1:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "4-5-6" and numero_uscito in terzina_2:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "7-8-9" and numero_uscito in terzina_3:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "10-11-12" and numero_uscito in terzina_4:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "13-14-15" and numero_uscito in terzina_5:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "16-17-18" and numero_uscito in terzina_6:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "19-20-21" and numero_uscito in terzina_7:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "22-23-24" and numero_uscito in terzina_8:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "25-26-27" and numero_uscito in terzina_9:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "28-29-30" and numero_uscito in terzina_10:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "31-32-33" and numero_uscito in terzina_11:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        elif puntata == "34-35-36" and numero_uscito in terzina_12:
            print("Hai vinto!")
            credito += scommessa * 11
            return credito
        else:
            print("Hai perso!")
            return credito
    else:
        print("Scelta non valida.")
        return credito
                      
def main():
    global credito
    numero = ruota()
    
    valore_scommessa, valore_puntata, valore_scelta = scommessa()
    #print(f"Hai scommesso {valore_scommessa}€ su {valore_puntata}")
    
    altre_puntate = input("Vuoi fare altre puntate? ne puoi fare fino a 3 (s/n) ")
    if credito > 0: 
        if altre_puntate == "s":
            valore_scommessa2, valore_puntata2, valore_scelta2 = scommessa()
            #print(f"Hai scommesso {valore_scommessa2}€ su {valore_puntata2}")
            altre_puntate2 = input("Vuoi fare altre puntate? ne puoi fare ancora una (s/n) ")
            
            
            if credito > 0:
                if altre_puntate2 == "s":
                    valore_scommessa3, valore_puntata3, valore_scelta3 = scommessa()
                    #print(f"Hai scommesso {valore_scommessa3}€ su {valore_puntata3}")
                    print("Ottimo, hai fatto 3 puntate! Allora via alle danze!")
                    animazione_ruota(numero)
                    credito1 = vincita(valore_scommessa, valore_puntata, valore_scelta, numero)
                    credito = credito1
                    credito2 = vincita(valore_scommessa2, valore_puntata2, valore_scelta2, numero)
                    credito = credito2
                    credito3 = vincita(valore_scommessa3, valore_puntata3, valore_scelta3, numero)
                    credito = credito3                   
            else:
                print("Non hai abbastanza credito per fare altre puntate.")
                time.sleep(1)
                print("Ottimo, hai fatto 2 puntate! Allora via alle danze!")
                animazione_ruota(numero)
                credito1 = vincita(valore_scommessa, valore_puntata, valore_scelta, numero)
                credito = credito1
                credito2 = vincita(valore_scommessa2, valore_puntata2, valore_scelta2, numero)
                credito = credito2
                credito3 = 0                        
    else:
        print("Non hai abbastanza credito per fare altre puntate.")
        time.sleep(1)
        print("Ottimo, hai fatto 1 puntata! Allora via alle danze!")
        animazione_ruota(numero)
        credito1 = vincita(valore_scommessa, valore_puntata, valore_scelta, numero)
        credito2 = 0    
        credito3 = 0
        credito = credito1
            
    time.sleep(2)
    print(f"Il tuo credito è di {credito}€ \n")
    return credito


print("Benvenuto! Fai anche tu una partita alla ciroulette, la roulette virtuale dove non si perde mai!")
time.sleep(1)
print("Per oggi hai un'offerta esclusiva: 100€ di credito per iniziare da subito a giocare e divertirti!.")
time.sleep(1)
print("Prova e vedrai che non te ne pentirai, parola di ciro. \nBuona Fortuna!")
time.sleep(1)

decisione = input("Allora, vuoi giocare? (s/n) ")

if decisione == "s":
    while True:
        credito = main()
        if credito <= 0:
            print("Hai perso tutto!")
            time.sleep(2)
            break
        else:
            risposta = input("Vuoi continuare a giocare? (s/n) ")
            if risposta == "n":
                print("Grazie per aver giocato, arrivederci!")
                break
else:
    print("Peggio per te, si vede che non hai coraggio...")

input("Premi invio per uscire...")