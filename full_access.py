# rôle Data Scientist
# Accès complet : modèle + prédiction sur texte brut

import pickle
from utils.text_processing import clean_text

# Chargement du modèle, du vectorizer et de la fonction nécessaire
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
    
with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

vectorizer = tfidf  # Ici on simule l'accès avec le vectorizer global

# Exemple d'utilisation complète
message = "Congratulations! You've won a prize."
message_clean = clean_text(message)
vectorized = vectorizer.transform([message_clean])
pred = model.predict(vectorized)
print("[DATA SCIENTIST] Prédiction :", "SPAM" if pred[0] else "HAM")