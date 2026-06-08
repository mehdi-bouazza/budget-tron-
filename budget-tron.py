# begin prompt
print ("Welkom bij budget-tron, vul je gegevens in om je basis casflow-outlay the bereken en te bepalen")

# prompt om inkomsten op te vragen
salaris = float(input("Wat is je salaris?: "))
pm = int(input ("Hoeveel uur werk je?: "))
salarisuur = round(salaris / (pm * 52 / 12))
print(f"Je bruto-uurloon is {salarisuur}")

# validatie verzamelinkomen
if salaris > 4139: 
 print(f"Let op! Je verdient {4139-salaris} meer dan het verzamelinkomen")
else: 
 print(f"je zit in de veilige zone")

#prompt om basiskosten op vragen
huisvesting = int(input("Maandelijke uitgaven voor huur/hypotheek?: "))
kosten_huisvesting = (huisvesting / salaris * 100)
if kosten_huisvesting <= 35:
    print(f"je geeft {kosten_huisvesting}% uit en dit is < 35% van je inkomen")
elif kosten_huisvesting == 35:
    print(f"je geeft {kosten_huisvesting} uit en dit is 35%")
else:
    rest_huisvesting = (kosten_huisvesting - 35)
    print(f"je geeft {kosten_huisvesting}% van je salaris aan je huisvesting uit! en dit is {rest_huisvesting}% boven de signaalwaarde")
    
voedsel = int(input("Maandelijkse uitgaven voor voedsel?: "))
zelfzorg = int(input("Maandelijkse uitgaven voor zelfzorg en schoonmaakproducten?: "))
gwl = int(input("Maandelijkse uitgaven voor GWL?: "))
zorgverzekering = int(input("Maandelijkse uitgaven voor de zorgverzekering?: "))
maandelijkse_uitgaven = (huisvesting + voedsel + zelfzorg + gwl + zorgverzekering)
print(f" je geeft in totaal: {maandelijkse_uitgaven} uit")

# Geeft terug hoeveel euro's je nominaal en procentueel uitgeeft van je inkomen
cash_uit = (huisvesting + voedsel + zelfzorg + gwl + zorgverzekering)
kostenprofiel = (cash_uit / salaris * 100)
if kostenprofiel >= 60:
    print(f"je geeft {kostenprofiel}% uit en dit is meer dan 60%, herzie je cijfers")
else:
    print(f"je geeft: {kostenprofiel}% uit van je salaris aan vaste lasten:")
if kostenprofiel <=60: 
    print(f"je kan {salaris - kostenprofiel} sparen")












