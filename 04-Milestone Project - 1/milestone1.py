def printBoard(board):
    for i in range(0,3,1):
        for j in range(0,3,1):
            print(board[i][j],end=" ")
        print('\n')

def checkResult(board):
    t=0
    i=0
    if i in range(0,3,1):
        if board[i][0]=='X' and board[i][1]=='X' and board[i][2]=='X':
            t=1
        elif board[i][0]=='Y' and board[i][1]=='Y' and board[i][2]=='Y':
            t=2
        elif board[0][i]=='X' and board[1][i]=='X' and board[2][i]=='X':
            t=1
        elif board[0][i]=='Y' and board[1][i]=='Y' and board[2][i]=='Y':
            t=2
        else:
            t=0
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        t=1
    if board[0][0] == 'Y' and board[1][1] == 'Y' and board[2][2] == 'Y':
        t=2
    return t
        
#Player input
player1=input("Please pich X or O as 1st player: ")
player2 =""
if player1 == 'X':
    player2='O'
else:
    player2='X'

TikTokBoard = [['_','_','_'],['_','_','_'],['_','_','_']]
mapping = {0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],6:[2,0],7:[2,1],8:[2,2]}
print("Welcone to the Game\n")
printBoard(TikTokBoard)
t=0
while True:
    move = int(input('Enter you move: '))
    x=mapping[move][0]
    y=mapping[move][1]
    if t%2==0:
        TikTokBoard[x][y]='X'
    else:
        TikTokBoard[x][y]='O'
    t=t+1
    printBoard(TikTokBoard)
    x=checkResult(TikTokBoard)
    if x == 0:
        continue
    elif x == 1:
        print('Player one is winner')
        break
    elif x == 2:
        print('Player two wins')
        break

## ************** Thank you for playing the game ******************





