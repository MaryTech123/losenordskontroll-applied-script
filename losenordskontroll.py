
# Importerar biblioteket getpass, för att läsa in lösenord utan att visa det i terminalen
import getpass

#Funktion för att kontrollera lösenord: tar emot lösenord och kontrollerar säkerhetskraven
def kontrollera_losenord(losenord):

#Jag antar att lösenordet är starkt från början och om någon krav inte uppfylls, då är det FALSE
    starkt=True

#Kontroll 1: Nu kontrollerar jag om lösenordet är längre än 12 tecken, om det är kortare än 12, är det svagt lösenord:
    if len(losenord) < 12:
        print ("FEL: ditt lösenordet är kortare än 12 tecken.")
        starkt= False

# Nu gör jag kontroll 2: om det finns stor bokstav i lösenordet. islower är TRUE om alla bokstäver är små, då betyder det att det finns ingen stor bokstav.
    if losenord.islower():
      print ("FEL: ditt lösenord innehåller ingen stor bokstav.")
      starkt= False

# Nu gör jag kontroll 3: om det finns en siffra i lösenordet. Jag använder any () som kontrollerar om minst ett tecken är en siffra. Om ingen sifra hittas, lösenordet är SVAGT.

    if not any(tecken.isdigit() for tecken in losenord):
         print ("FEL: ditt lösenord innehåller ingen siffra.")
         starkt= False

    return starkt


#Skriver rubriken
print ("Kontroll av ditt lösenord:")

# Läser in lösenord från användaren,  getpass gör att texten inte syns när man skriver
losenord = getpass.getpass("Skriv ditt lösenord (det visas inte på skärmen): ")

#Anropar funktionen som kontrollerar lösenordet, resultatet (true eller false) sparas i variabeln starkt
starkt = kontrollera_losenord(losenord)

#Skriver ut rubrik för resultaten:
print ("Resultat: ")

#Om starkt är TRUE, kontrollerna klarades
if starkt:
        print ("Lösenordet är Godkänt!! Grattis! Ditt lösenord uppfyller alla krav.")
else: # Om Starkt är FALSE, kontrollen mislyckades och lösenordet är svag.
	print ("Lösenordet är SVAGT, du borde ändra det.")

