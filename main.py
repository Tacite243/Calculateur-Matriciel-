import os
from function import *

"""""
Projet de conception d'un calculateur matricielle
Projet à réaliser dans le cadre de cloture de la première
année de licence, en faculté des sciences et technologies appliquées
Groupe n°22

"""""

matrice1 = []
matrice2 = []

on = True

def request():
    print("Taper sur 'Q' pour quitter"
          " ou sur 'R' pour relancer l'application")

    request = None
    while request == None:
        try:
            request = str(input("==) "))
        except TypeError:
            print("Vous avez entré une valeur éronnée")
            request = None
        except ValueError:
            print("Vous avez entré une valeur éronnée")
            request = None

    if request == 'Q' or 'q':
        os.system("cls")
        afficher_function()
    elif request == 'q' or 'Q':
        os.system("cls")
        return exit()
    else:
        os.system("cls")
        return afficher_function()


while on == True:
    def afficher_function():
        print("BIENVENUE DANS LE LOGICIEL DU GROUPE 22")
        print("**" * 30)
        print("Quelle opération voulez-vous éffectuer?")
        print("**" * 30, "\n")
        print("1. Addition de deux matrices\n"
              "2. Multiplication de deux matrices\n"
              "3. Multiplication d'une matrice par un scalaire\n"
              "4. Rechercher le mineure\n"
              "5. Transposer la matrice\n"
              "6. Trouver le coffacteur\n"
              "7. Trouver la trace\n"
              "8. Calculer le déterminant\n"
              "9. Vérifier l'égalité de deux matrices\n"
              "10. Calculer la matrice puissance \n"
              "11. Inverser une matrice\n"
              "12. Calculer la commatrice")
        print("**" * 30)

        answer = input("===) ")

        # verification erreur

        try:
            answer = int(answer)
        except ValueError:
            print("La valeur indiqué n'est pas correct")

        if answer == 1:
            os.system("cls")
            print("**" * 30)
            print("ADDITION DES MATRICES\n", "**" * 30, "\n"
                  "Veuillez entrez les matrices à additionner")
            print("**" * 30, "\n")

            # matrice 1

            lgn, cln = demande_dimension()

            print("**" * 30, "\n")

            matrice1 = creation_matrice(lgn, cln)
            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            # matrcice 2
            print("Entrez les éléments de la deuxième matrice")

            matrice2 = creation_matrice(lgn, cln)
            print("Matrice B")
            afficher_matrice(matrice2)

            print("--" * 30)

            sum = addition_matrices(matrice1, matrice2)
            print("La matrice somme est:\n")
            afficher_matrice(sum)

            request()

        elif answer == 2:
            print("**" * 30)
            print("MULTIPLICATION DE 2 MATRICES")
            print("**" * 30)

            # matrcice1

            print("Entrez les éléments de la première matrice\n")

            lgn1, cln1 = demande_dimension()

            print("--" * 30)

            matrice1 = creation_matrice(lgn1, cln1)
            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            # matrice2

            lgn2, cln2 = demande_dimension()

            print("--" * 30)

            matrice2 = creation_matrice(lgn2, cln2)
            print("Matrice B")
            afficher_matrice(matrice2)

            print("--" * 30)

            produit = multipli(matrice1, matrice2)
            print("La matrice produuit est:\n")
            afficher_matrice(produit)

            request()

        elif answer == 3:
            print("**" * 30)

            print("MULTIPLICATION D'UNE MATRICE PAR UN SCALAIRE")

            print("**" * 30, "\n")
            print("Entrez le scalaire")
            scalaire = None
            while scalaire == None:
                try:
                    scalaire = float(input("==)"))
                except ValueError:
                    scalaire = None

            print("--" * 30)

            lgn, cln = demande_dimension()

            print("--" * 30)

            matrice = creation_matrice(lgn, cln)

            print("--" * 30)

            print("Matrice A")
            afficher_matrice(matrice)

            print("--" * 30)

            produit = multipli_scalaire(matrice, scalaire)
            print("La matrice A X", scalaire, " égale\n")
            afficher_matrice(produit)

            request()

        elif answer == 4:
            print("**" * 30)

            print("CALCUL DE MINEUR D'UNE MATRICE")

            print("**" * 30)

            lgn1, cln1 = demande_dimension()

            print("--" * 30)

            matrice1 = creation_matrice(lgn1, cln1)
            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)
            print("Entrez les références de l'élément par"
                  "rapport auquel vous voulez calculer le mineur")
            num_lgn = None
            while num_lgn == None:
                try:
                    num_lgn = int(input("Entrez ici son numéro de ligne: "))
                except ValueError:
                    num_lgn = None
            num_cln = None

            print("--" * 30)

            while num_cln == None:
                try:
                    num_cln = int(input("intrez ici son numéro de colonne: "))
                except ValueError:
                    num_cln = None

            print("--" * 30)

            lgn = num_lgn - 1
            cln = num_cln - 1
            operation = recherche_de_mineure(matrice1, lgn, cln)
            print("\n", "le mineur est:", "\n", operation)

            request()

        elif answer == 5:
            print("**" * 30)

            print("TRANSPOSITION D'UNE MATRICE")

            print("**" * 30)

            lgn1, cln1 = demande_dimension()
            matrice = creation_matrice(lgn1, cln1)

            print("--" * 30)

            print("Matrice A")
            afficher_matrice(matrice)

            print("--" * 30)

            operation = transpose(matrice)
            print("La transposée de la matrice A est:\n")
            afficher_matrice(operation)

            request()

        elif answer == 6:
            print("**" * 30)

            print("RECHERCHE DE COFACTEUR D'UNE MATRICE")

            print("**" * 30)

            lgn1, cln1 = demande_dimension()
            matrice1 = creation_matrice(lgn1, cln1)

            print("--" * 30)

            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            print("Entrez le numéro de la ligne et de la colonne\n"
            "de l'élément par rapport auquel vous voulez calculer le coffacteur")

            num_lgn = None
            num_cln = None

            print("--" * 30)
            while num_lgn == None:
                try:
                    num_lgn = int(input("1. Numéro de la ligne: "))
                except ValueError:
                    num_lgn = None
            print("--" * 30)
            while num_cln == None:
                try:
                    num_cln = int(input("2. Numéro de la colonne: "))
                except ValueError:
                    num_cln = None
            print("--" * 30)

            operation = cofacteur(matrice1, num_lgn, num_cln)
            print("Le cofacteur de la matrice A est:")
            print(operation)

            request()

        elif answer == 7:

            print("**" * 30)

            print("RECHERCHE DE LA TRACE D'UNE MATRICE")

            print("**" * 30)

            lgn1, cln1 = demande_dimension()

            print("--" * 30)

            matrice1 = creation_matrice(lgn1, cln1)

            print("--" * 30)

            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            operation = fonction_trace(matrice1)
            print("La trace de la matrice A est:")
            print(operation)

            request()

        elif answer == 8:
            print("**" * 30)

            print("CALCUL DU DETERMINANT")

            print("**" * 30)

            lgn1, cln1 = demande_dimension()
            print("--" * 30)

            matrice1 = creation_matrice(lgn1, cln1)

            print("--" * 30)

            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            operation = determinant_general(matrice1)
            print("La déterminant de la matrice A est\n", operation)

            request()

        elif answer == 9:
            print("**" * 30)

            print("VERIFICATION DE L'EGALITE DE 2 MATRICES")

            print("**" * 30, "\n")

            # Matrice1

            print("ENTREZ D'ABORD LA PREMIERE MATRICE")
            print("--" * 30)

            lgn1, cln1 = demande_dimension()

            print("--" * 30)

            matrice1 = creation_matrice(lgn1, cln1)

            print("--" * 30)
            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            # Matrice2

            print("ENTREZ LA SECONDE MATRICE")

            lgn2, cln2 = demande_dimension()
            print("--" * 30)

            matrice2 = creation_matrice(lgn2, cln2)

            print("--" * 30)
            print("Matrice B")
            afficher_matrice(matrice2)

            print("--" * 30)

            # Vérification

            operation = compare_matrice(matrice1, matrice2)

            request()

        elif answer == 10:
            print("**" * 30)

            print("CALCULER LA PUISSANCE Nième D'UNE MATRICE")

            print("--" * 30)

            print("Entez la puissance:")
            n = None
            while n == None:
                try:
                    n = int(input("===) "))
                except ValueError:
                    n = None

            print("--" * 30)

            lgn, cln = demande_dimension()

            print("--" * 30)

            matrice1 = creation_matrice(lgn, cln)

            print("--" * 30)

            print("Matrice A")
            afficher_matrice(matrice1)

            print("--" * 30)

            if cln == lgn:
                m_exp = matrice_expos_n(matrice1, n)
                print("La matrice A exposant", n, " est:\n")
                afficher_matrice(m_exp)
            else:
                print("Opération impossible pour cette matrice")

            request()

        elif answer == 11:
            print("**" * 30)

            print("INVERSION D'UNE MATRICE")

            print("**" * 30)

            lgn, cln = demande_dimension()

            print("--" * 30)

            matrice = creation_matrice(lgn, cln)

            print("--" * 30)

            print("La matrice inverse de A est:\n")
            print(inverser_matrice(matrice))

            request()

        elif answer == 12:
            print("**" * 30)

            print("RECHERCHE DE LA COMATRICE")

            print("**" * 30)
            lgn, cln = demande_dimension()

            print("--" * 30)

            matrice = creation_matrice(lgn, cln)
            print("La comatrice de la matrice A est:")
            afficher_matrice(comatrice(matrice))

            request()

        else:
            print("--" * 30)
            print("Valeur invalide")
            request()

    afficher_function()
    request()

os.system("pause")