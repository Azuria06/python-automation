import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.trustpilot.com/review/tripadvisor.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"❌ Erreur {response.status_code} : Accès refusé.")
        exit()

    soup = BeautifulSoup(response.text, "html.parser")

    avis_list = []
    for i, avis in enumerate(soup.find_all("div", class_="review-card")):
        if i >= 10:  # Limite à 10 avis
            break

        nom = avis.find("span", class_="consumer-name").text.strip()
        note = avis.find("div", class_="star-rating").text.strip()
        commentaire = avis.find("p", class_="review-text").text.strip()

        avis_list.append([nom, note, commentaire])

    df = pd.DataFrame(avis_list, columns=["Nom", "Note", "Commentaire"])
    df.to_excel("avis_clients.xlsx", index=False)

    print("✅ Scraping terminé, fichier avis_clients.xlsx mis à jour.")

except Exception as e:
    print(f"❌ Erreur lors du scraping : {e}")