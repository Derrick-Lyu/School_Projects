import copy
import random
import numpy as np

def rollDice(Ndice, NSide):
    alist = []
    for curDice in range(Ndice):
        cur_output = random.randint(1,NSide)
        alist.append(cur_output)
    #print(alist)
    return alist

def chooseDice(state, loseCount, winCount, nDice, M):
    X = state[0]
    Y = state[1]

    f_list = [-100]
    p_list = [-100]*(nDice+1)

    T = 0
    for num_Dice in range(1,nDice+1):
        T += loseCount[num_Dice][X][Y]+winCount[num_Dice][X][Y]
        if (loseCount[num_Dice][X][Y]+winCount[num_Dice][X][Y]) == 0:
            f_j = 0.5
        else:
            f_j = winCount[num_Dice][X][Y]/(loseCount[num_Dice][X][Y]+winCount[num_Dice][X][Y])
        f_list.append(f_j)
    best_move= f_list.index(max(f_list))
    #rint("best Move is", best_move)
    g = sum(f_list[1:])-f_list[best_move]
    p_list[best_move] = (T*f_list[best_move] + M) / (T*f_list[best_move]+nDice*M)
    for num_Dice in range(1,nDice+1):
        if num_Dice != best_move:
            p_list[num_Dice] = (1-p_list[best_move]) * ((T*f_list[num_Dice]+M)/(g*T+(nDice-1)*M))
    #print("f_list", f_list, "\np_list", p_list)
    best_choice = random.choices(range(1,nDice+1),p_list[1:])[0]
    return best_choice

def PlayGame(nDice, nSides, lTarget, uTarget, loseCount, winCount, M):
    player1 = []
    player1_state = [0,0]
    player1_score = 0
    player2 = []
    player2_state = [0,0]
    player2_score = 0
    count = 1
    who_win = 0 # 1-> player 1 win; 2->player 2 win
    #playing actural game
    while True:
        if count%2 == 1: #player 1 round
            count+=1
            best_move = chooseDice(player1_state,loseCount,winCount,nDice,M)
            #best_move = random.randint(1,nDice)
            cur_dice_outcome = rollDice(best_move, nSides)
            player1_score += sum(cur_dice_outcome)
            cur_xyj = copy.deepcopy(player1_state)
            cur_xyj.append(best_move)
            player1.append(cur_xyj)
            """print("player 1 has rolled %d dice, and the current outcome of the dice is %s, he got %d score in total, "
                  "player1 = %s"
                  ""%(best_move,cur_dice_outcome, player1_score,str(player1)))"""
            # update state for both player
            player1_state[0] = player1_score
            player2_state[1] = player1_score
            #print(player1_state,player2_state)
            if player1_score > uTarget:
                who_win = 2
                break
            elif player1_score >= lTarget:
                who_win = 1
                break
        else: #player 2 round
            count += 1
            best_move = chooseDice(player2_state, loseCount, winCount, nDice, M)
            #best_move = random.randint(1, nDice)
            cur_dice_outcome = rollDice(best_move, nSides)
            player2_score += sum(cur_dice_outcome)
            cur_xyj = copy.deepcopy(player2_state)
            cur_xyj.append(best_move)
            player2.append(cur_xyj)
            """print("player 2 has rolled %d dice, and the current outcome of the dice is %s, he got %d score in total, "
                  "player2=%s"
                  "" % (best_move, cur_dice_outcome, player2_score, str(player2)))"""
            # update state for both player
            player2_state[0] = player2_score
            player1_state[1] = player2_score
            #print(player1_state, player2_state)
            if player2_score > uTarget:
                who_win = 1
                break
            elif player2_score >= lTarget:
                who_win = 2
                break
        #break
    #print("%d finally wins"%(who_win))
    #update winCount and lose count
    if who_win == 1:
        for xyj in player1:
            X = xyj[0]
            Y = xyj[1]
            J = xyj[2]
            winCount[J][X][Y] += 1
        for xyj in player2:
            X = xyj[0]
            Y = xyj[1]
            J = xyj[2]
            loseCount[J][X][Y] += 1
    else:
        for xyj in player1:
            X = xyj[0]
            Y = xyj[1]
            J = xyj[2]
            loseCount[J][X][Y] += 1
        for xyj in player2:
            X = xyj[0]
            Y = xyj[1]
            J = xyj[2]
            winCount[J][X][Y] += 1
    #print(winCount)
    #print("------------")
    #print(loseCount)
    return winCount,loseCount

def extractAnswer(winCount,loseCount,lTarget,nDice,M):
    best_strategies = np.zeros((lTarget,lTarget))
    best_strategies_prob = np.zeros((lTarget,lTarget))
    for row in range(lTarget):
        for column in range(lTarget):
            temp_max, temp_max_value = 0, 0
            for num_dice in range(1,nDice+1):
                if winCount[num_dice][row][column] > temp_max_value:
                    temp_max_value = winCount[num_dice][row][column]
                    temp_max = num_dice
            best_strategies[row][column] = temp_max
            if(winCount[temp_max][row][column]+loseCount[temp_max][row][column])==0:
                best_strategies_prob[row][column] = 0
            else:
                best_strategies_prob[row][column] = winCount[temp_max][row][column]/\
                                                    (winCount[temp_max][row][column]+loseCount[temp_max][row][column])
    print("Play=\n", best_strategies, "\nProb=\n", best_strategies_prob)
    return best_strategies,best_strategies_prob

def prog3(nDice,nSides,lTarget,uTarget,nGames,M):
    loseCount = np.zeros((nDice + 1, lTarget, lTarget))
    winCount = np.zeros((nDice + 1, lTarget, lTarget))
    for i in range(nGames):
        #print("---------------------------New Game----------------------------")
        PlayGame(nDice, nSides, lTarget, uTarget, loseCount, winCount, M)
    extractAnswer(winCount,loseCount,lTarget,nDice,M)

def main():
    nDice = int(input("Enter number of Dice\n"))
    nSides = int(input("Enter Number of Sides\n"))
    lTarget = int(input("Enter Lower Target\n"))
    uTarget = int(input("Enter Upper Target\n"))
    nGames = int(input("Enter Number of Games\n"))
    M = int(input("Enter number of M\n"))

    prog3(nDice,nSides,lTarget,uTarget,nGames,M)


if __name__ == "__main__":
    main()