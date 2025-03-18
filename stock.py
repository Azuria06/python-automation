import pandas as pd
import os
import requests

FILE_PATH = "stock.xlsx"
API_URL = "https://api.exemple.com/update_stock"

# Vérifier si le fichier existe
if not os.path.exists(FILE_PATH):
    print(f"❌ Erreur : {FILE_PATH} introuvable.")
    exit()

try:
    df = pd.read_excel(FILE_PATH)
    df["Statut"] = "En attente"

    for index, row in df.iterrows():
        payload = {"produit": row["Produit"], "quantite": row["Quantité"]}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            df.at[index, "Statut"] = "Mise à jour OK"
        else:
            df.at[index, "Statut"] = f"Échec {response.status_code}"

    df.to_excel("stock_updated.xlsx", index=False)
    print("✅ Mise à jour des stocks terminée.")

except Exception as e:
    print(f"❌ Erreur lors du traitement : {e}")