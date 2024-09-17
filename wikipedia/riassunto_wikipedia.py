#Importazione delle librerie necessarie
from googletrans import Translator
from wikipedia import summary, set_lang, search, exceptions

#Definizione del traduttore e della lingua
traduttore = Translator()
lingua = input("Che lingua parli? (it/en) ") 

# Imposta la lingua per le ricerche su Wikipedia
try:
    set_lang(lingua)
except:
    print("Lingua non supportata")
    exit() 


# Definisce i testi da utilizzare nelle interfacce utente
testi = [
    "Che pagina vuoi cercare?", 
    "Ho trovato questi risultati:", 
    "Scegli quale pagina vuoi cercare(inserisci il numero corrispondente):", 
    "Nessuna pagina trovata",
    "Premi invio per uscire"
]

# Se la lingua è inglese, traduce i testi
if lingua == "en":
    testi[0] = traduttore.translate(testi[0], dest="en").text
    testi[1] = traduttore.translate(testi[1], dest="en").text
    testi[2] = traduttore.translate(testi[2], dest="en").text
    testi[3] = traduttore.translate(testi[3], dest="en").text
    testi[4] = traduttore.translate(testi[4], dest="en").text
    

#Ricerca della pagina, stampa dei risultati
ricerca = input(testi[0] + " ")
risultati = search(ricerca) 

print("\n" + testi[1] + " " + str(risultati) + "\n")

if len(risultati) == 0:
    print(testi[3])
    exit()  


#Scelta della pagina e stampa del riassunto
pagina = int(input(testi[2] + " ")) - 1

try:
    riassunto = summary(risultati[pagina])
    print("\n" + riassunto)
except exceptions.PageError:
    print(testi[3])

input(testi[4])

