# start

# vakna
vaken = "n" # Sätter variabeln "n" till vaken
print("du sover djupt som björnen i ide...") # Skriver ut det som står mellan dubbelfnuttarna i programmet
while vaken == "n": #loopar rad 7 så länge vaken = "n"
    vaken = input("vaknar du? [y/n] ").lower() # väljer om du är vaken eller inte, skriver du "n" kommer du tillbaka till rad 7 igen. Skriver du y eller annan bokstav går du vidare i programmet.

# duscha
print("Gå och duscha")
print("Någon har lämnat en brödrost i duschen")

duscha = input("flyttar du på brödrosten? [y/n] ").lower() # Berättar för programmet vilken väg vi tar i resten av programmet

if duscha == "n": # Om svaret på rad 13 är "n" får vi en elstöt enligt rad 16 och programmet stängs av
    print("du får en elstöt i duschen och ligger och krampar på golvet de närmaste dagarna tills någon hittar dig")
    exit("Game over LOSER!") # stänger av programmet
elif duscha == "y": # Om svaret på rad 13 är y går du vidare i programmet till rad 25 och får meddelandet från rad 19
    print("Du blir äntligen ren efter gårdagens kaos.")
else:
    print("Skriv y eller n nästa gång") # Om du varken skriver "y" eller "n" avslutas programmet enligt rad 22
    exit()

# årstid
season = False # Sätter "season"s standardvärde till false
while season == False: # Så länge "season == false" kommer loopen backa tillbaka till rad 26
    season = input("vilken årstid är det? [vår, vinter, sommar, höst]").lower() # Skriv in vilken årstid. ".lower()" gör så att alla bokstäver är små bokstäver
    if season == "vår" or season == "vinter" or season == "höst": # Om det är vår, höst eller vinter kommer följande 2 rader printas ut
        print("det är kallt och slaskigt")
        print("du tar på dig alla kläder i garderoben")
    elif season == "sommar": # Om vi skriver sommar på rad 27 kommer du hit och rad 32 printas ut i konsollen
        print("Det är skitvarmt ute, överväger att gå naken")
    else: # Om du skriver något annat än en årstid eller stavar fel, kommer du tillbaka till rad 26 eftersom rad 34 ger värdet "season = false" igen
        season = False

# Ta sig till skolan
resa = False
while resa == False:
    resa = input("hur tar du dig till skolan? [hoverboard, rollerscates, rymdraket, teleportör]").lower()
    if resa == "hoverboard":
        print("Du blir mobbad för att du har för lite clout, blir nedslagen och dödad")
    
    elif resa == "rollerscates":
        print("Du får punktering på ett däck och hamnar på trottoarkanten, där ser du en clown i kloakerna med en röd ballong, du syns aldrig igen")
    
    elif resa == "rymdraket":
        print("Trodde du på riktigt att du skulle ta dig till skolan i en raket? Du är dummare än du ser ut.")
    
    elif resa == "teleportör":
        print("Du vet inte vart du hamnar, men du står framför 2 aliens som spelar in porr, du joinar och tjänar en förmögenhet på en annan planet")
    
    else:
        season = False