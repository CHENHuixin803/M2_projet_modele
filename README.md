# Projet de Simulation en Hémodynamique
**Cours :** Modèles mathématiques appliqués à la biologie

**Auteur :** CHEN Huixin(21319577)

## Structure du Projet

Ce dépôt contient les codes sources pour le projet de simulation en hémodynamique. Les fichiers ont été organisés pour correspondre aux exercices du sujet.

| Fichier | Description |
| :--- | :--- |
| **`Ex1_CrosseAortique.edp`** | Simulation de l'écoulement dans la crosse aortique (affichage en temps réel) |
| **`Ex1_CrosseAortique_Data.edp`** | Simulation de la crosse aortique et extraction des données `.txt` (Pression et Débit) |
| **`Ex1_Q4b_Plot.py`** | Script Python pour tracer l'évolution des pressions et débits (Question 1.4b) |
| **`Ex1_Q4c_Fit.py`** | Script Python pour l'ajustement linéaire et le calcul de la résistance cible (Question 1.4c) |
| **`Ex2_Bifurcation.edp`** | Simulation de l'écoulement dans la bifurcation (affichage en temps réel) |
| **`Ex2_Bifurcation_Data.edp`** | Simulation de la bifurcation et extraction des données `.txt` pour les deux sorties |

### Comment utiliser
1. Exécutez les fichiers `_Data.edp` avec FreeFem++ pour générer les fichiers de données `.txt`.
2. Exécutez les scripts `.py` correspondants avec Python (nécessite `pandas` et `matplotlib`) pour générer et sauvegarder les graphiques.
