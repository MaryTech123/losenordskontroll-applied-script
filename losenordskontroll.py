
# Importerar biblioteket getpass, för att läsa in lösenord utan att visa det i terminalen
import getpass

#Funktion för att kontrollera lösenord: tar emot lösenord och kontrollerar säkerhetskraven
def kontrollera_losenord(losenord):

#Jag antar att lösenordet är starkt från början och om någon krav inte uppfylls, då är det FALSE
    starkt=True

#Kontroll 1: Nu kontrollerar jag om lösenordet är längre än 12 tecken, om det är kortare än 12, är det svagt lösenord:
    if len(losenord) < 12:
        print ("FEL: lösenordet är kortare än 12 tecken")
        starkt= False

    return starkt

#Skriver rubriken
print ("Kontroll av ditt lösenord:")

# Läser in lösenord från användaren,  getpass gör att texten inte syns när man skriver
losenord = getpass.getpass("Skriv ditt lösenord (det visas inte): ")

#Anropar funktionen som kontrollerar lösenordet, resultatet (true eller false) sparas i variabeln starkt
starkt = kontrollera_losenord(losenord)

#Skriver ut rubrik för resultaten:
print ("Resultat: ")

#Om starkt är TRUE, kontrollen klarades
if starkt:
        print ("Lösenordet är Ok!")
else: # Om Starkt är FALSE, kontrollen mislyckades och lösenordet är svag.
	print ("Lösenordet är SVAGT.")



