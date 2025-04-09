# Interface utilisateur avec authentification et chiffrement des prédictions
import streamlit as st
import pickle
from cryptography.fernet import Fernet
from utils.text_processing import clean_text

# Chargement du modèle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Chargement du vectorizer
with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)
    
vectorizer = tfidf  # À adapter si le vectorizer est stocké séparément

# Chargement de la clé de chiffrement
with open("fernet.key", "rb") as kf:
    key = kf.read()
fernet = Fernet(key)

# Authentification simulée
PASSWORD = "admin123"
user_input = st.text_input("Mot de passe", type="password")

if user_input == PASSWORD:
    st.success("Authentification réussie !")
    sms = st.text_area("Entrer un SMS à analyser :")

    if sms:
        cleaned = clean_text(sms)
        vect = vectorizer.transform([cleaned])
        pred = model.predict(vect)[0]
        result = "SPAM" if pred else "HAM"

        # Chiffrement du résultat
        encrypted_result = fernet.encrypt(result.encode()).decode()

        st.write(f"Prédiction : {result}")
        st.code(f"Résultat chiffré : {encrypted_result}", language='text')
else:
    st.warning("Veuillez entrer un mot de passe pour accéder à l'interface.")