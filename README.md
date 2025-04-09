# Projet : Détection de SMS spam avec Pipeline NLP sécurisé

## 🔍 Objectif
Mettre en place un pipeline NLP de classification des SMS (spam vs ham) pour une entreprise, tout en assurant la **sécurité des données**, du **modèle**, et de l'**environnement d'exécution**.

## 🧱 Structure du projet
```
Projet_SMS_Protect/
├── data/
│   └── sms.tsv
├── notebooks/
│   ├── pipeline_nlp_securisation.ipynb
├── scripts/
│   ├── full_access.py
│   └── analyst_access.py
├── streamlit_app/
│   └── streamlit_app.py
├── model/
│   ├── model.pkl
│   ├── model_hash.txt
│   └── fernet.key
```

## 🔁 Étapes du pipeline
1. **Nettoyage NLP** : minuscule, suppression stopwords, lemmatisation
2. **Vectorisation** : TF-IDF
3. **Modélisation** : Logistic Regression
4. **Évaluation** : classification report, matrice de confusion

## 🔐 Sécurisation
- **Chiffrement des données sensibles** avec `Fernet`
- **Vérification de l'intégrité du modèle** avec `hashlib` (SHA256)
- **Contrôle des accès** via scripts simulant les rôles (Data Scientist / Analyste)
- **Résultat chiffré** via interface Streamlit

## ▶️ Lancer l'interface utilisateur
```
streamlit run streamlit_app.py
```
Mot de passe : `admin123`

## 📌 Auteurs
Maxime HOU - IA DS3