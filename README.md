# 16_NLP_analyse_critiques_films
Dans ce brief, il est question d'analyser le sentiment à travers des critiques en français de spectateurs sur des films.

## Contexte du projet
En règle générale, le nombre d'avis sur un film peu être important et par conséquent le temps de lecture de chaque commentaire peut être une tâche lourde. Alors comment déterminer de manière rapide si un film a eu du succès auprès des spectateurs (ou pas) ? Dans ce contexte, l’idée du projet est d’utiliser des algorithmes d'apprentissage automatique pour la tâche d'analyse de sentiment des spectateurs via leur critique.

**************************************************************************************************************
**Les étapes à réaliser :**
- Récupération des données 
- Préparation des données
- Préparation du modèle et des jeux de données (entrainement & test) 
- Analyse des résultats

**************************************************************************************************************
## Documents dans ce GitHub :
### 1) le rapport *.pdf :
qui documente et explique les différentes étapes du notebook

### 2) 1 notebook NLP_critiques_films_inception_sonic2.ipynb :
avec les différentes étapes : 
  - Etape 1 - Web Scraping des données d’avis de spectacteurs
  - Etape 2 - Préparation des données : suppression des RegEx, les tokens, stopwords, bag of words, ...
  - Etape 3 - Préparation des libellés : X et y, jeu d'apprentissage et test
  - Etape 4 - Finalisation de nos jeux de données : CountVectorizer, affichage de WordCloud
  - Etape 5 - Entraînement du modèle : Régression logistique
  - Etape 6 - Analyse des résultats : Accuracy, matrice de confusion
  - en sus : Essais avec vectorisation de TF-IDF

### 3) Appli_WebScraping.py :
fichier python exécutant le code de webscraping, y compris la sauvegarde sous forme de csv

### 4) les fichiers *.csv des avis 
















