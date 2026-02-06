# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""

FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]
NOMBRE_LIGNES = 10
sections = ["A", "B", "C", "D", "E", "F", "G", "H"]
intensites = []
niveaux = []
nombres_personnes = []
try:
    for i in range(len(sections)):
        nombres_personnes.append(int(input(f"Entrez le nombre de personnes dans la section {sections[i]} : ")))
    
    
    for i in range(len(nombres_personnes)):
        if nombres_personnes[i] < 0:
            print("Erreur - donnees invalides.")
            exit()
    for i in range(len(FACTEURS)):
        intensites.append(nombres_personnes[i] * FACTEURS[i])
    
    max_intensite = max(intensites) 
    
    for i in range(len(sections)):
        if max_intensite == 0:
            niveaux = [0]*8 
        else: 
            niveaux.append(int((intensites[i] / max_intensite) * 10 + 0.5)) 
    
    for niveau_ligne in range(NOMBRE_LIGNES,0,-1):
        print(f"{niveau_ligne:>2} |", end = "") 
        for colonnes in range(len(sections)):
            if niveaux[colonnes] >= niveau_ligne:
                print(" ❚", end = "")
            else:
                print(" .", end = "")
        print("")
    
    print("     A B C D E F G H")    

except ValueError:
    print("Erreur - donnees invalides.")