# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)
nbr_billet = int(input("Entrez le nombre de billets necessaires : "))
statut  = input("Entrez le statut etudiant (O/N) : ")

# TODO: Validation (n >= 0 et statut dans {O, N})
if nbr_billet < 0 or (not statut == "O" and not statut == "N"):
    print("Erreur - donnees invalides.")
else:
    nbr_billet_init = nbr_billet 
    billets_24, billets_12, billets_5, billet_uni = 0,0,0,0 
    
    while nbr_billet_init >= 24:
        billets_24 += 1
        nbr_billet_init = nbr_billet_init-24
    while nbr_billet_init >= 12:
        billets_12 += 1
        nbr_billet_init = nbr_billet_init-12 
    while nbr_billet_init >= 5:
        billets_5 += 1
        nbr_billet_init = nbr_billet_init-5 
    while nbr_billet_init > 0: 
        billet_uni += 1
        nbr_billet_init = nbr_billet_init-1 
    
    if statut == "O":
        prix = (billets_24*66 + billets_12*36 + billets_5*15.75)*0.88 + billet_uni*3.6 
    else:
        prix = (billets_24*66 + billets_12*36 + billets_5*15.75 + billet_uni*3.6) 
    
    print(f"Forfaits de 24 billets - {billets_24},Forfaits de 12 billets - {billets_12},Forfaits de 5 billets - {billets_5},Billets unitaires - {billet_uni},Total billets - {nbr_billet},Prix total - {prix:.2f}$".replace(",", "\n") )
 

