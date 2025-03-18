import pandas as pd

# Charger le fichier en ignorant la première ligne
df = pd.read_excel("stock.xlsx", skiprows=1)

# Ajouter une colonne "Statut"
df["Statut"] = "Mise à jour OK"

# Sauvegarder le fichier mis à jour
df.to_excel("stock_updated.xlsx", index=False)

print("✅ Stock mis à jour et sauvegardé dans 'stock_updated.xlsx'.")