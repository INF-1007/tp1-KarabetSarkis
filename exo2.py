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
sections = ["A", "B", "C", "D", "E", "F", "G", "H"]
intensite=[]
niveau = []

try: 
    for i in range(8):
        nombres_personnes = int(input(f"Personnes dans les sections {sections[i]}? "))
        if nombres_personnes < 0:
            print("Erreur - donnees invalides.") 
            break
        else:
            intensite.append(nombres_personnes * FACTEURS[i])
            max_i = max(intensite) 
            if max_i == 0:
                niveau = 0
            else:
              niveau.append(int((intensite[i]/ max_i) * 10 + 0.5))
                
    for i in range(10,0,-1):
        print(f"{i:>2} |", end = "")  
        for j in range(len(sections)):
                if i <= niveau[j]:
                    print("❚ ", end = "")
                else:
                    print(". ", end = "")
        print("")
    print("    A B C D E F G H")

except ValueError:
    print("Erreur - donnees invalides.")


