


class Board:

    def __init__(self):
        self.winner=False
        self.tie=False
        self.board=[' ',' ',' ', ' ',' ',' ', ' ',' ',' ']


    def print_board(self):
        print(self.board[0], " | ",self.board[1], " | ", self.board[2])
        print("-------------")
        print(self.board[3], " | ",self.board[4], " | ", self.board[5])
        print("-------------")
        print(self.board[6], " | ",self.board[7], " | ", self.board[8])

    def player_1(self):
        while not self.winner and not self.tie:
            turn1= int(input("Input a number from 1-9 depending on where you want to play: "))
            if turn1 not in [1,2,3,4,5,6,7,8,9]:
                print("Invalid input, try again")
                return self.player_1()
            elif self.board[turn1-1]!=" ":
                print("that space is taken, try again")
                return(self.player_1())
            else:
                self.board[turn1-1]="X"
                (self.print_board())
                break



    def player_2(self):
        while not self.winner and not self.tie:
            turn2=int(input("Input a number from 1-9 that is not taken: "))
            if turn2 not in [1,2,3,4,5,6,7,8,9]:
                print("Invalid input, try again")
                return self.player_2()
            elif self.board[turn2-1]!=" ":
                print("that space is taken, try again")
                return(self.player_2())
            else:
                self.board[turn2-1]="O"
                (self.print_board())
                break


    def check_winner(self):
        #checking winner for rows
        for i in range(0,9,3):
            if self.board[i]==self.board[i+1]==self.board[i+2] and self.board[i]!=" ":
                if self.board[i]=="X":
                    print("X wins!")
                else:
                    print("O wins!")
                self.winner=True

        #checking winner for columns
        for i in range(0,3):
            if self.board[i]==self.board[i+3]==self.board[i+6] and self.board[i]!=" ":
                if self.board[i]=="X":
                    print("X wins!")
                else:
                    print("O wins!")
                self.winner=True


          #checking winner for diagonals
        if (self.board[0]==self.board[4]==self.board[8] and self.board[0]!=" " ) or (self.board[2]==self.board[4]==self.board[6] and self.board[2]!=" "):
            self.winner=True
            if self.board[4]=="X":
                print("X wins!")
            else:
                print("O wins!")


    def check_tie(self):
        if self.board.count(" ")==0 and not self.winner:
            print("game is a tie")
            self.tie=True


    def game(self):
        while not self.winner and not self.tie:
            self.player_1()
            self.check_winner()
            self.check_tie()
            self.player_2()
            self.check_winner()
            self.check_tie()





board1 = Board()
board1.print_board()
board1.game()

