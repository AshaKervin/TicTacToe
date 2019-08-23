import functions

print("Welcome to Tic Tac Toe!")
print("Here's the current board:")


functions.displayBoard()

isPlaying = True
while(isPlaying==True):

    functions.play("Player1")
    print("Move accepted, here's the current board: ")
    isPlaying = functions.findWinner();
    functions.displayBoard()
    functions.play("Player2")
    print("Move accepted, here's the current board: ")
    isPlaying = functions.findWinner();
    functions.displayBoard()
   
