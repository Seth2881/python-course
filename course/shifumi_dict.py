import random as tartiflette

def bot() :
    temp  = tartiflette.choices(["rock","paper","scissors"],k=1)
    return temp[0]

def player() :
    temp = input("'rock','paper' or 'scissors' ? (case sensitive) : ")
    if temp not in ["rock","paper","scissors"]:
        player()
    return temp

def whoWin(bot,player,points) :
    win_cond = {
        "rock" : "scissors", #rock gagne contre scissors
        "paper" : "rock",    #paper gagne contre rock
        "scissors" : "paper" #scissors gagne contre paper
    }
    #retourne le score en fonction des inputs du bot et du joueur
    return [points[0]+1,points[1]] if( win_cond[bot] == player)else([points[0],points[1]+1] if(bot!=player)else(score))

score = [0,0]

while not 2 in score :
    score = whoWin(bot(),player(),score)
    print('bot :',score[0],'player :',score[1])

print('Great job ! You won !') if(score[1]==2)else(print('You loose to the AI'))