game = ['.','.','.'],['.','.','.'],['.','.','.']

def gameBoard():
    for row in game:
        print(row[0],row[1],row[2])

def play(player):
    needQuestion = True
    while(needQuestion == True):
        print(player," Enter a coord x,y to place your X or enter 'q' to give up: ",end="");
        playerInput = input();
        if (playerInput == 'q'):
            print("Bye!");
            exit(0)
        if (len(playerInput)!=3):#only numbers 1,2,3 can be used
            print("Invalid input. Try again.");
            continue
        if (playerInput[1] != ","):
            print("Invalid input. Try again.");
            continue
        try:
            x = int(playerInput[0])
            y = int(playerInput[2])
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
            continue
        if (x>3 or y>3 ):
            print("Invalid input. Try again.");
            continue
        if (x<1 or y<1 ):
            print("Invalid input. Try again.");
            continue
        if (game[x-1][y-1] == 'O' or game[x-1][y-1] == 'X'):
            print("Oh no, a piece is already at this place! Try again...")
            needQuestion = True
        else:
            needQuestion = False
            if player == "player1" : game[x-1][y-1]='X'
            else : game[x-1][y-1]='O'

def endGame(player):
    gameBoard()
    if player == "draw":      
        print("Draw!")
        exit(0)
    print("Well Done! The Winner is",player)
    exit(0)

def winner():
    #Horizontal alignment of either X or O is a win
    for row in game:
        if row[0]==row[1]==row[2]=='X':
            endGame("player1")
        if row[0]==row[1]==row[2]=='O':
            endGame("player2")
    #Vertical alignment of either X or O is a win        
    for coloum in [0,1,2]:
        if game[0][coloum]==game[1][coloum]==game[2][coloum]=='X':
            endGame("player1")
        if game[0][coloum]==game[1][coloum]==game[2][coloum]=='O':
            endGame("player2")
    #diagonal1 alignment is a win
    if game[0][0]==game[1][1]==game[2][2]=='X':
        endGame("player1")
    if game[0][0]==game[1][1]==game[2][2]=='O':
        endGame("player2")
    #diagonal2 alignment is a win
    if game[2][0]==game[1][1]==game[0][2]=='X':
        endGame("player1")
    if game[2][0]==game[1][1]==game[0][2]=='O':
        endGame("player2")
    #draw occurs when there is no winner and all fields are taken on the board
    sumOfPoint=[]
    for row in game:
        for item in row:
            sumOfPoint.append(item)
    if sumOfPoint.count('.') == 0:
        endGame("draw")
    return True
    
