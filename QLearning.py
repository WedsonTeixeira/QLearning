from random import randint, random

# 0 = cima
# 1 = baixo
# 2 = esquerda
# 3 = direita

def populateEnvironment():
    environment = []
    for _ in range(6):
        line = []
        for _ in range(6):
            line.append([0,0,0,0])
        environment.append(line)
    return environment

def populateRewards():
    rewards = []
    for _ in range(6):
        line = []
        for _ in range(6):
            line.append(0)
        rewards.append(line)
    return rewards

ambiente = populateEnvironment()
recompensas = populateRewards()

# Estado do objetivo
inicialx = 4
inicialy = 5

# Recompensa para objetivo
recompensa = 10
recompensas[inicialx][inicialy] = recompensa


def max(list):
    maior = list[0]
    for i in list:
        if(i > maior):
            maior = i
    return maior

def position_max(list):
    position = 0
    maior = list[0]
    for i in range(len(list)):
        if(list[i] > maior):
            maior = list[i]
            position = i
    return position

def isFinalState(x, y):
    if recompensas[x][y] == 0:
        return False
    return True

def getStartLocation():
    x = randint(0,5)
    y = randint(0,5)

    while isFinalState(x,y):
        x = randint(0,5)
        y = randint(0,5)
    return x, y

def getNextLocation(currX, currY, action):
    newX = currX
    newY = currY
    #action = randint(0,3)
    if(action == 0 and currX != 0):
        newX -= 1
    elif(action == 1 and currX != 5):
        newX += 1
    elif(action == 2 and currY != 0):
        newY -= 1
    elif(action == 3 and currY != 5):
        newY += 1
    return newX, newY

def getNextAction(currX, currY, probability):
    if random() < probability:
        return position_max(ambiente[currX][currY])
    oldX = currX
    oldY = currY
    action = None
    while currX == oldX and currY == oldY:
        action = randint(0,3)
        currX, currY = getNextLocation(currX, currY, action)
    return action

def main():
    for i in range(1000):
        currX, currY = getStartLocation()

        while not isFinalState(currX, currY):
            action = getNextAction(currX, currY, 0.)
            oldX, oldY = currX, currY
            currX, currY = getNextLocation(oldX, oldY, action)

            recompensa = recompensas[currX][currY]
            new_valor_movimento = recompensa + (0.8 * max(ambiente[currX][currY]))

            ambiente[oldX][oldY][action] = round(new_valor_movimento, 3)
    
    # local que vou sair para ir ao objetivo
    saindox = 1
    saindoy = 1

    caminho = []

    while(not isFinalState(saindox,saindoy)):
        caminho.append((saindox,saindoy))
        action = getNextAction(saindox, saindoy, 1)
        saindox, saindoy = getNextLocation(saindox, saindoy, action)
    
    caminho.append((inicialx,inicialy))
    print(caminho)
    
   
main()