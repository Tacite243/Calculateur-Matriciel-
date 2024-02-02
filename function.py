import os

"""
    fonction demandant à l'utilisateur de de 
    donner les dimmensions de sa matrice
"""

def demande_dimension():
    nombre_des_colonnes = None
    nombre_des_lignes = None
    while (nombre_des_lignes == None):
        try :
            nombre_des_lignes = int(input("Entrez le nombre de lignes : "))
        except ValueError :
            nombre_des_lignes = None
    while (nombre_des_colonnes == None):
        try :
            nombre_des_colonnes = int(input("Entrez le nombre de colonnes : "))
        except ValueError :
            nombre_des_colonnes = None

    return nombre_des_colonnes, nombre_des_lignes


"""
    fonction permettant la création d'une matrice
"""

def creation_matrice(nbr_lignes, nbr_colonnes):
    matrice = []
    for i in range(nbr_lignes):
        ligne = []
        for j in range(nbr_colonnes):
            ligne.append(0)
        matrice.append(ligne)

    for i in range(nbr_lignes):
        for j in range(nbr_colonnes):
            matrice[i][j] = None
            while matrice[i][j] == None:
                try:
                    matrice[i][j] = float(input(f"Tapez l'élément numéro {j+1} de la ligne numéro {i+1} : "))
                except ValueError:
                    matrice[i][j] = None
    return matrice

"""
    fonction permettant de formater l'affichage
    d'une matrice
"""

def afficher_matrice(matrice):
    for i in matrice:
        try:
            i = i
        except TypeError:
            print()
        print(f"{i}")

"""
    fonction verifiant les dimensions d'une matrice
"""

def verification_nbr_lign_col(matrice):
    lignes = len(matrice)
    colonnes = len(matrice[0])

    return lignes, colonnes

"""
    fonction renvoyant la somme de deux matrices
"""

def addition_matrices(m1, m2):
    ligne, col = verification_nbr_lign_col(m1)

    m = [[m1[i][j] + m2[i][j] for j in range(col)] for i in range(ligne)]
    return m
def soustraction_matrices(m1,m2):
    ligne, col = verification_nbr_lign_col(m1)
    soustraction = [[m1[i][j] - m2[i][j] for j in range(col)] for i in range(ligne)]
    return soustraction
"""
    fonction renvoyant le produit de deux matrices
"""

def multipli(matrice1, matrice2):
    nbr_lgn_matr1, nbr_cln_matr1 = verification_nbr_lign_col(matrice1)
    nbr_lgn_matr2, nbr_cln_matr2 = verification_nbr_lign_col(matrice2)

    if nbr_cln_matr1 != nbr_lgn_matr2:
        print("La multiplication entre ces deux matrices n'est pas possible!\n")
        print("--"*10, "\n"
              "Tapez sur 'Q' si vous vous voulez quiter et sur 'R' si vous voulez recommencer\n")
        answer = input("==) ")
        if answer == "Q" or "q":
            quit()
        elif answer == "R" or "r":
            request = demande_dimension()
            print(request)
        else:
            quit()
        os.system("pause")

    elif nbr_cln_matr1 == nbr_lgn_matr2:
        resultat = [[0] * nbr_cln_matr2 for i in range(nbr_lgn_matr1)]
        for i in range(nbr_lgn_matr1):
            for j in range(nbr_cln_matr2):
                for k in range(nbr_lgn_matr2):
                    resultat[i][j] += matrice1[i][k] * matrice2[k][j]
        return resultat

"""
    fonction renvoyant la copie d'une matrice
"""

def creer_copy(matrice):
    matrice_copy = []
    for i in range(len(matrice)):
        matrice_copy.append([0]*(len(matrice[0])))
        for j in range(len(matrice[0])):
            matrice_copy[i][j] = matrice[i][j]
    return matrice_copy

"""
    fonction calculant le mineure d'une matrice
"""
def recherche_de_mineure(matrice, k, l):
    # Fonction pour calculer les mineurs
    copy_matrice = creer_copy(matrice)
    lignes, _ = verification_nbr_lign_col(copy_matrice)
    for i in range(lignes):
        del copy_matrice[i][l]
    del copy_matrice[k]
    det_minor = determinant_general(copy_matrice)

    return det_minor

"""
    fonction permettant de renvoyer une matrice unité
"""

def matrice_unite(dimension):
    matrice = []
    for i in range(dimension):
        matrice.append([0]*(dimension))
        for j in range(dimension):
            if (i == j):
                matrice[i][j] = 1
    return matrice

"""
    fonction permettant de calculer la puissance nième d'une matrice
"""
def matrice_expos_n(matrice, n):
    ligne, colonne = verification_nbr_lign_col(matrice)
    if (ligne == colonne):
        matri_expo = matrice_unite(ligne)
        for i in range(n):
            matri_expo = multipli(matri_expo, matrice)
        return matri_expo
    else:
        print("Votre matrice n'est pas carrée")
        return None

"""
    fonction vérifiant l'égalité de deux matrices
"""

def compare_matrice(matrice1, matrice2):
    if (matrice1 == matrice2):
        print("Les deux  matrices sont égales")
    else:
        print("les deux matrices sont différentes")

"""
    fonction renvoyant le signe de (-1) selon
    le nombre mis en parramètre 
"""
def fonction_signe(i, j):
    """Le i et j ne peuvent pas etre 0"""
    signe = (-1)**(i+j)
    return signe

"""
    fonction calculant le déterminant d'une matrice
    d'ordre générale d'une matrice
"""
def determinant_general(matrice):
    lignes, colonnes = verification_nbr_lign_col(matrice)
    if (lignes == colonnes):
        determ = 0
        if (lignes == 1):
            determ = matrice[0][0]
        else:
            for j in range(colonnes):
                i = 0
                # On prend la ligne 0
                determ += fonction_signe(i+1, j+1)*matrice[i][j]*recherche_de_mineure(matrice, i, j)
        return determ

    else:
        print("La matrice n'est pas carrée")
        return None

# Fonction de la trace d'une matrice

def fonction_trace(matrice):
    # Fonction trace
    nombre_des_lignes, nombre_des_colonnes = verification_nbr_lign_col(matrice)
    trace = 0
    for i in range(nombre_des_lignes):
        for j in range(nombre_des_colonnes):
            if i == j:
                trace += matrice[i][j]
            else:
                pass
    return trace

# fonction permettant de calculer la transposée d'une matrice

"""
    fonction renvoyant la multiplication 
    d'une matrice par un scalaire
"""

def multipli_scalaire(matrice, c):
    lgn, cln = verification_nbr_lign_col(matrice)
    for i in range(lgn):
        for j in range(cln):
            C = float(c)
            matrice[i][j] *= C
    return matrice
def division_par_un_scalaire(matrice ,b):
    lgn, cln = verification_nbr_lign_col(matrice)
    for i in range(lgn):
        for j in range(cln):
            B = float(b)

            matrice[i][j] /= B
    return matrice

""""
    fonction gerant les erreurs
"""

def cofacteur(matrice, i, l):
    minor = recherche_de_mineure(matrice, i, l)
    if i+l % 2 == 0:
        return minor
    else:
        return - minor

def creer_matrice_nulle(lines, columns):
    matrice = []
    for i in range(lines):
        line = []
        for j in range(columns):
            line.append(0)
        matrice.append(line)
    return matrice

def transposition(matrice):
    lines, columns = demande_dimension()
    transpose = creer_matrice_nulle(columns, lines)
    for j in range(lines):
        for i in range(columns):
            transpose[i][j] = matrice[j][i]

    return transpose

def transpose(matrice):
    lgn, cln = verification_nbr_lign_col(matrice)
    trans = []
    for j in range(cln):
        unit = []
        for i in range(lgn):
            unit.append(matrice[i][j])
        trans.append(unit)
    return trans

def inverser_matrice(matrice):
    lgn, cln = verification_nbr_lign_col(matrice)
    if cln == lgn:
        com = comatrice(matrice)
        t_com = transpose(com)
        det_a = determinant_general(matrice)
        try :
            scalaire = 1 / det_a
        except ZeroDivisionError :
            print("Matrice non inversible")

        inverse = multipli_scalaire(t_com, scalaire)
        afficher_matrice(inverse)
    else:
        os.system("pause")

def comatrice(matrice):
    n = len(matrice)
    com = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            com[i][j] = cofacteur(matrice, 1, 1)
    return com