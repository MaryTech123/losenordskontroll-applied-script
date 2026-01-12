
# Applied Script projekt
## Lösenordskontroll
Detta projekt kontrollerar ifall den angivna lösenord är säkert eller osäkert enligt olika säkerhetskrav. För att ha en godkänt och starkt lösenord måste det innehålla:
* Minst 12 tecken
* Minst en stor bokstav
* Minst en siffra
* Minst en specialtecken
* Inte vara inkluderat i rockyou filen

Om inte dessa kravs uppfylls, kommer scriptet visa ett _felmeddelandet_ och generera en *nytt starkt lösenord* som uppfyller alla krav.

### Syfte / Mål

Syftet med detta script är att stärka användarnas säkerhet genom att analysera svaga lösenord innan de används och erbjuda en ny säkert och starkt lösenord istället. 

Det här lösenordskontroll bidrar till att minska risken för kontokapningar eller brute-force attacker. Det bidrar till bättre medvetandet inom säkerhet och  uppmuntra till goda lösenordsvanor.

### Funktion

#### Main 
Scriptet kontrollerar om lösenordet uppfyller följande krav:
* Minst 12 tecken
* Minst en stor bokstav
* Minst en siffra
* Minst en specialtecken
* Inte vara inkluderat i rockyou filen
#### Branch 1: Generera ny lösenord

Om användarens lösenord är svag, skapar scripten en ny lösenord som uppfyller alla krav.

#### Branch 2: Kontroll mot rockyou.txt

Scriptet kontrollerar ifall användarens lösenord finns på rockyou.txt filen.

### Systemkrav
Linux  (Kali Linux)  
Terminal åtkomst  
Git och Github   
Rockyou.txt filen   
Python 3  
Standard Python bibliotek:  
* getpass
* random
* string  


### Instruktioner
1. Klona repository
https://github.com/MaryTech123/losenordskontroll-applied-script.git  
cd losenordskontroll
2. Starta scriptet  
python3 losenordskontroll.py
3. Följ instruktioner i terminalen

### Flödesschema

https://miro.com/app/board/uXjVGUcOtbc=/

[Marias Flödesschema](https://miro.com/welcomeonboard/cVdtRDVFek8rTzJ3UW1ndlNmSlRLUHZNeWxLQnpLNHJNZTgwNWlNS09teTFzRTNhZUw5U3RKY1RqMmcvNTMxdG1KVVRHZEhsRmRYZFRmdWhleUhQelRCODRhWXBSczIxR0MxTkV6c1pDaUV3MUNJM05rcHM4RGZwUlI0czhxZWp3VHhHVHd5UWtSM1BidUtUYmxycDRnPT0hdjE=?share_link_id=728594219406)


### Screenshot/ Film

## Tom was here !
