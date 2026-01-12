
#1 IMPORTS

# Importerar biblioteket getpass, för att läsa in lösenord utan att visa det i terminalen
import getpass

#Jag importerar random, för att kunna välja slumpmässiga tecken
import random

# jag importerar string, som innehåller färdiga grupper av tecken, tx. bokstäver, siffor och speciella tecken.
import string


#2 FUNKTIONER

#Funktion för att kontrollera lösenord: tar emot lösenord och kontrollerar säkerhetskraven
def kontrollera_losenord(losenord):

#Jag antar att lösenordet är starkt från början och om någon krav inte uppfylls, då är det FALSE
    starkt=True

#Kontroll 1: Nu kontrollerar jag om lösenordet är längre än 12 tecken, om det är kortare än 12, är det svagt lösenord:
    if len(losenord) < 12:
        print ("FEL: ditt lösenord är kortare än 12 tecken.")
        starkt= False

# Nu gör jag kontroll 2: om det finns stor bokstav i lösenordet. islower är TRUE om alla bokstäver är små, då betyder det att det finns ingen stor bokstav.
    if losenord.islower():
      print ("FEL: ditt lösenord innehåller ingen stor bokstav.")
      starkt= False

# Nu gör jag kontroll 3: om det finns en siffra i lösenordet. Jag använder any () som kontrollerar om minst ett tecken är en siffra. Om ingen sifra hittas, lösenordet är SVAGT.

    if not any(tecken.isdigit() for tecken in losenord):
         print ("FEL: ditt lösenord innehåller ingen siffra.")
         starkt= False

# Kontroll 4: Kontrollerar om det finns en specialtecken eller ej. Jag använder isalnum() som returnerar TRUE om lösenordet innehåller bara tecken och siffror, inga speciellatecken.
    if losenord.isalnum():
         print ("FEL: ditt lösenord innehåller inga specialtecken.")
         starkt= False

#Här returnerar funktionen resultatet (true= starkt lösenord, false= svagt lösenord)
    return starkt

#Skapar en funktion som genererar ett slumpmässigt lösenord

def generera_slumpmassigt_losenord():
     
     #Här bestämmer jag vilka tecken som kan användas i lösenordet: ascii_letters (små+stora bokstäver) + digits (0-9) + punctuation (speciellatecken)
     tillatna_tecken=string.ascii_letters + string.digits + string.punctuation

     # Här bestämmer jag hur långt lösenordet ska vara
     losenord_langd = 14

     # Vi börjar med ett tomt lösenord utan text

     nytt_losenord = ""

     # Nu gör jag en loop som körs en gång per tecken (14 varv)
     for i in range(losenord_langd):
          
          slump_tecken= random.choice(tillatna_tecken) #Här väljer ett slumpmässigt tecken från de tillåtna tecken

          nytt_losenord= nytt_losenord + slump_tecken # Här lägger jag till teckenet sist i lösenordet

    
    #När hela loopen är klar, returnerars det lösenordet

     return nytt_losenord

#Branch 2: Kontrollerar om lösenordet finns i rockyou.txt
def finns_i_rockyou(losenord):
     
     #Öppnar rockyou.txt från Kali-wordlist-mappen
     fil = open("/usr/share/wordlists/rockyou.txt", errors="ignore") #skriver errors=ignore då annars krascher programmet pga.olika konstiga tecken.

     #läser filen rad för rad
     for rad in fil:
          #strip() tar bort radbrytning 
          if rad.strip() == losenord:
               #Om lösenordet skulle hittas i listan, filen stängs och returneras True
               fil.close()
               return True
     fil.close()
     return False
     

#3 MAIN/PROGRAMFLÖDE

#Skriver rubriken till scriptet
print ("Nu kontrolleras ditt lösenord:")

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

#Branch 2: 
if finns_i_rockyou(losenord):
     print("VARNING: Ditt lösenord finns i rockyou.txt filen! Ditt lösenord är mycket osäkert!")
     starkt= False #Detta markerar lösenord som svag, så att nytt lösenord föreslås


# Branch 1: föreslå nytt lösenord
if not starkt:
     print ("Här är ditt förslag på ett godkänt och starkare lösenord som fyller alla krav och inte finns i rockyou filen:")
     print (generera_slumpmassigt_losenord())


#Tom was here




