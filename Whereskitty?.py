import sopel.module

@sopel.module.commands('kitty')

from random import randint

board = []

for x in range(5):
     board.append(["O"] * 5)

 def show_board(board):
     for row in board:
         bot.say( " ".join(row))

# def play_game(bot, trigger):

#     bot.say "Where's the kitty?"
#     show_board(board)

#     def random_row(board):
#        return randint(0, len(board) - 1)

#     def random_col(board):
#         return randint(0, len(board[0]) - 1)

#     ship_row = random_row(board)
#     ship_col = random_col(board)


#     for turn in range(4):
#         guess_row = int(raw_input("Guess Row:"))
#         guess_col = int(raw_input("Guess Col:"))

#         if guess_row == ship_row and guess_col == ship_col:
#             print "Congratulations! You found the kitty =^..^=!"
#             break
#         else:
#             if (guess_row < 0 or guess_row > 4) \
#             or (guess_col < 0 or guess_col > 4):
#                 print "Oops, you've wandered outside of the discernable universe."
#                 if turn == 3:
#                     print "Game Over! Kitty reigns supreme!"
#             elif(board[guess_row][guess_col] == "X"):
#                 print "You've already guessed that spot."
#                 if turn == 3:
#                     print "Game Over! Kitty reigns supreme!"
#             else:
#                 print "Kitty still eludes you."
#                 board[guess_row][guess_col] = "X"
#                 if turn == 3:
#                     print "Game Over! Kitty reigns supreme!"
#         print "Turn", turn + 1
#         print 
#         show_board(board)