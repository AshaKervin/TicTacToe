import functions

print("Welcome to Tic Tac Toe!")
print("Here's the current board:")

functions.gameBoard()

isPlaying = True
while(isPlaying==True):
    functions.play("player1")
    print("Move accepted, here's the current board: ")
    isPlaying = functions.winner();
    functions.gameBoard()
    functions.play("player2")
    print("Move accepted, here's the current board: ")
    isPlaying = functions.winner();
    functions.gameBoard()
   
    