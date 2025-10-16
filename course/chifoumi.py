from random import randint

def botChoose() :
    nbr = randint(1,3)
    return "pierre" if nbr == 1 else ("feuille" if nbr == 2 else ("ciseaux"))

def playerChoose() :
    shifumi = input("pierre, feuille ou ciseaux ? : ")
    shifumi.lower()
    if shifumi in ["pierre","feuille","ciseaux"] :
        return shifumi
    else :
        print(f'[!] {shifumi} : syntaxe incorrecte')
        playerChoose()

win_player = 0
win_bot = 0

while win_player<2 and win_bot<2 :
    
    bot_shifumi = botChoose()
    player_shifumi = playerChoose()

    if not(player_shifumi == bot_shifumi) :
        
        if bot_shifumi == 'pierre' :
            if player_shifumi == 'ciseaux' :
                win_bot += 1
            else : 
                win_player += 1

        elif bot_shifumi == 'feuille' :
            if player_shifumi == 'pierre' :
                win_bot += 1
            else :
                win_player += 1
        
        elif bot_shifumi == 'ciseaux' :
            if player_shifumi == 'feuille' :
                win_bot += 1
            else :
                win_player += 1
        
        print(f'bot : {win_bot} ; joueur : {win_player}')
    else :
        print('égalité !')

print(f'le bot as gagné {win_bot} à {win_player}') if win_bot == 2 else (print(f'Tu as gagné {win_player} à {win_bot} !'))