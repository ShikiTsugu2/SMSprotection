#rôle Analyste
# Accès limité : uniquement prédiction sur texte déjà vectorisé

import pickle

# Supposons que l'analyste reçoive un message déjà transformé (sécurité renforcée)
# Ici, on ne donne pas accès aux fonctions de nettoyage ni au modèle brut

# Chargement du modèle pour prédiction uniquement
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Simulation : prédiction sur vecteur donné (ex : transmis par API sécurisée)
# Exemple : message prétraité = "congratulation win prize"
vectorized_input = tfidf.transform(["congratulation win prize"])
prediction = model.predict(vectorized_input)
print("[ANALYSTE] Prédiction reçue :", "SPAM" if prediction[0] else "HAM")