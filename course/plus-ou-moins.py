# from random import randint as filsdepute
# def difficulte() : choose_dif = int(input('1 : facile, 2 : moyen, 3 : difficile : '));return filsdepute(0,100) if choose_dif == 1 else (return filsdepute(0,1000) if choose_dif == 2 else (return filsdepute(0,10000) if choose_dif == 3 else (difficulte())))
# def plusoumoins(nbr) : nbr_user = int(input("Devinez le nombre !"));return(print("vous avez trouvé !")) if nbr_user == nbr else(print("C'est moins !"),plusoumoins(nbr) if nbr_user > nbr else (print("C'est plus !"),plusoumoins(nbr)))
# plusoumoins(difficulte())

from random import randint as filsdepute

attemps = 0

def difficulte() :
    choose_dif = int(input('1 : facile, 2 : moyen, 3 : difficile : '))
    if choose_dif == 1 :
        nbr = filsdepute(0,100)
        return nbr
    elif choose_dif == 2 :
        nbr = filsdepute(0,1000)
        return nbr
    elif choose_dif == 3 :
        nbr = filsdepute(0,10000)
        return nbr
    else :
        difficulte()

def plusoumoins(nbr) :
    global attemps
    attemps += 1
    nbr_user = int(input("Devinez le nombre : "))
    if nbr_user == nbr : 
        print(f"vous avez trouvé en {attemps} attemps !")
        return
    elif nbr_user > nbr :
        print("C'est moins !")
        plusoumoins(nbr)
    elif nbr_user < nbr :
        print("C'est plus !")
        plusoumoins(nbr)

plusoumoins(difficulte())