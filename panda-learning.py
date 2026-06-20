import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Importeren van de brondata ("r" achter "(" voorkomt fouten in pathfinding)
df = pd.read_csv(r"x", sep=';', decimal=',')

# Datacleaning (Maand als maand importeren)
df['Maand'] = pd.to_datetime(df['Maand'], format='%d-%m-%Y')
df['Maandnummer_Schoon'] = df['Maand'].dt.to_period('M').astype(str)

# Basis om de kolommen te zien, zodat je kan checken of je bestand goed ingeladen is.
print(df.columns)

# Basis om de kolommen te zien, zodat je kan checken of je bestand goed ingeladen is.

# Basis om de 1e 5 rijen te zien, zodat je kan checken of je bestand goed ingeladen is.

print(df.head())

# Beschrijvende statistiek in 1 functie.

print(df.describe())

# Om datadimensies (nom, ord etc) te koppelen maak je variabelen en sla je je data op als een variabele. Oefening 1: Ik wil weten wat mijn nominale brutoprijs is voor gas per maand?

gasverbruik= df['Gas (m3)']
gasprijs= df['Gasprijs (m3)']

nomgas_maand = gasverbruik * gasprijs
df['Nominale_Gaskosten'] = nomgas_maand

# Opgezette datadimensie bekijken
print(nomgas_maand)

# Bereken het gemiddelde (alle kosten bij elkaar opgeteld gedeeld door het aantal maanden)
gemiddelde_kosten = nomgas_maand.mean()

# Bereken de mediaan (het exacte middelste getal als je de kosten van laag naar hoog sorteert)
mediaan_kosten = nomgas_maand.median()

# Uitkomsten strak op je scherm met twee decimalen 
print(f"Gemiddelde gaskosten per maand: € {gemiddelde_kosten:.2f}")
print(f"Mediaan van de gaskosten:        € {mediaan_kosten:.2f}")

# 3. Maak het venster lekker breed
plt.figure(figsize=(12, 5))

# 4. Teken de barplot met de schone tekstkolom. 
sns.barplot(data=df, x='Maandnummer_Schoon', y='Nominale_Gaskosten', color='#f0bf4c')

# 5. Draai de labels 45 graden, zodat ze niet meer overlappen
plt.xticks(rotation=45, ha='right')

# 6. Titels en layout strak trekken 
plt.title('Nominale Gaskosten per Maand (Zonder Lege Data)', fontsize=14, fontweight='bold')
plt.xlabel('Tijdlijn (Jaar-Maand)', fontsize=12)
plt.ylabel('Kosten in Euro (€)', fontsize=12)

plt.tight_layout()
plt.axhline(y=10, color='red', linestyle='--', linewidth=2, label='Voorschotplafond')


# Groene streeplijn voor het gemiddelde
plt.axhline(y=gemiddelde_kosten, color='green', linestyle='--', linewidth=2, label=f'Gemiddelde (€ {gemiddelde_kosten:.2f})')

# Oranje streeplijn voor de mediaan
plt.axhline(y=mediaan_kosten, color='orange', linestyle='-.', linewidth=2, label=f'Mediaan (€ {mediaan_kosten:.2f})')

# Zorg dat de legenda links- of rechtsboven in de grafiek verschijnt
plt.legend()
plt.show()




