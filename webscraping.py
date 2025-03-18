import requests
from bs4 import BeautifulSoup
import pandas as pd

# 🔹 URL de la page des avis (modifier selon le site)
URL = "https://www.trustpilot.com/review/example.com"

# 🔹 Récupération du contenu
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # 🔹 Extraction des avis (exemple Trustpilot, adapter selon le site)
    avis_list = []
    for avis in soup.find_all("div", class_="review-card"):
        nom = avis.find("span", class_="consumer-name").text.strip()
        note = avis.find("div", class_="star-rating").text.strip()
        commentaire = avis.find("p", class_="review-text").text.strip()

        avis_list.append([nom, note, commentaire])

    # 🔹 Sauvegarde dans Excel
    df = pd.DataFrame(avis_list, columns=["Nom", "Note", "Commentaire"])
    df.to_excel("avis_clients.xlsx", index=False)

    print("✅ Scraping terminé, fichier avis_clients.xlsx créé.")
else:
    print(f"❌ Erreur {response.status_code} : Impossible de récupérer la page.")