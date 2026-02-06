# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str) 

# TODO: Lire les 4 valeurs (int)
try:
    nom_complet = input("Entrez votre nom complet : ")
    matchs_football = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
    duree_football = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
    matchs_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
    duree_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : ")) 

    if matchs_football < 0  or matchs_soccer < 0:
        print("Erreur - donnees invalides.")
    elif duree_football <= 0 or duree_soccer <= 0:
        print("Erreur - donnees invalides.") 
    else:
        
        duree_football_heur = int((duree_football * matchs_football)/60) 
        duree_football_min_rest = duree_football * matchs_football - duree_football_heur*60 

        duree_soccer_heur = int((duree_soccer * matchs_soccer)/60) 
        duree_soccer_min_rest = duree_soccer * matchs_soccer - duree_soccer_heur*60

        duree_total_min = duree_football * matchs_football + duree_soccer * matchs_soccer
        duree_total_heur = int(duree_total_min/60) 
        duree_total_min_rest = duree_total_min - duree_total_heur*60
    
        print(f"Bonjour {nom_complet}") 
        print(f"Football (Carabins): {matchs_football} match(s), {duree_football_heur}h{duree_football_min_rest:02d} de visionnage")
        print(f"Soccer (Carabins): {matchs_soccer} match(s), {duree_soccer_heur}h{duree_soccer_min_rest:02d} de visionnage")
        print(f"Total: {duree_total_heur}h{duree_total_min_rest:02d}")

except ValueError:
    print("Erreur - donnees invalides.") 
    

