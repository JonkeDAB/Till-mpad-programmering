# start

# vakna
vaken = "n"
print("du sover djupt som björnen i ide...")
while vaken == "n":
    vaken = input("vaknar du? [y/n] ").lower()

# duscha
print("Gå och duscha")
print("Någon har lämnat en brödrost i duschen")

duscha = input("flyttar du på brödrosten? [y/n] ").lower()

if duscha == "n":
    print("du får en elstöt i duschen och ligger och krampar på golvet de närmaste dagarna tills någon hittar dig")
    exit()
elif duscha == "y":
    print("Du blir äntligen ren efter gårdagens kaos.")
else:
    print("Skriv y eller n nästa gång")
    exit()

# årstid
season = False
while season == False:
    season = input("vilken årstid är det? [vår, vinter, sommar, höst]").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("det är kallt och slaskigt")
        print("du tar på dig alla kläder i garderoben")
    elif season == "sommar":
        print("Det är skitvarmt ute, överväger att gå naken")
    else:
        season = False