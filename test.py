import pandas as pd
import requests
from bs4 import BeautifulSoup

# Test Pandas : Création d'un DataFrame simple
data = {"Nom": ["Alice", "Bob", "Charlie"], "Âge": [25, 30, 35]}
df = pd.DataFrame(data)
df.to_excel("test.xlsx", index=False)
print("✅ Pandas fonctionne : fichier Excel créé !")

# Test Requests : Récupérer une page web
response = requests.get("https://www.example.com")
print(f"✅ Requests fonctionne : Statut {response.status_code}")

# Test BeautifulSoup : Extraire le titre d'une page
soup = BeautifulSoup(response.text, "html.parser")
print(f"✅ BeautifulSoup fonctionne : Titre de la page -> {soup.title.string}")