# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

import math 


distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
attente_navette = float(input("Entrez le temps d'attente de la navette (en minutes) : "))
temps_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
controle = float(input("Entrez le temps de controle a l'entree (en minutes) : "))

if distance < 0 or attente_navette < 0 or temps_metro < 0 or controle < 0:
    print("Erreur - donnees invalides.")
else:
    marche = round(distance * 60 / 5 + controle, 0)
    navette = round(attente_navette + distance * 60 / 18 + controle, 0)
    metro   = round(temps_metro + controle, 0)

    if marche <= navette:
        if marche == navette:
            if marche <= metro:
                if marche == metro:
                    print("Egalite : marcher, navette et metro.")
                else:
                    print("Egalite : marcher et navette.")
            else:
                print("Option la plus rapide : metro.")
        else:
            if marche <= metro:
                if marche == metro:
                    print("Egalite : marcher et metro.")
                else:
                    print("Option la plus rapide : marcher.")
            else:
                print("Option la plus rapide : marcher.")
    else:
        if navette <= metro:
            if navette == metro:
                print("Egalite : navette et metro.")
            else:
                print("Option la plus rapide : navette.")
        else:
            print("Option la plus rapide : metro.")
        

          



