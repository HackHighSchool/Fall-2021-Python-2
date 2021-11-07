


class Board:
    winner=False
    def __init__(self):

        self.board=[
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]


    def print_board(self):
        for i in range(len(self.board)):
            if i!=0:
                print("- - - - - - - ")
            for j in range(len(self.board[i])):
                if j!=0:
                    print(" |", end=" ")
                if j==2:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j], end=" ")

    def player_1(self):
        turn1= int(input("Input a number from 1-9 depending on where you want to play: "))
        if turn1<1 or turn1>9:
            print("Invalid input, try again")
            return self.player_1()
        else:
            if turn1>=1 and turn1<=3:
                if self.board[0][turn1-1]==" ":
                    self.board[0][turn1-1]="X"
                else:
                    print("\nThat space is taken, please enter another number \n")
                    return self.player_1()

            elif turn1>=4 and turn1<=6:
                if self.board[1][turn1-4]==" ":
                    self.board[1][turn1-4]="X"
                else:
                    print("\nThat space is taken, please enter another number \n")
                    return self.player_1()

            else:
                if self.board[2][turn1-7]==" ":
                    self.board[2][turn1-7]="X"
                else:
                    print("\nThat space is taken, please enter another number \n")
                    return self.player_2()
            (self.print_board())

    def player_2(self):
        turn2=int(input("Input a number from 1-9 that is not taken: "))
        if turn2<1 or turn2>9:
            print("Invalid input, try again")
            return self.player_2()
        else:
            if turn2>=1 and turn2<=3:
                if self.board[0][turn2-1]==" ":
                    self.board[0][turn2-1]="O"
                else:
                    print("\nThat space is taken, please enter another number \n")
                    return self.player_2()
            elif turn2>=4 and turn2<=6:
                if self.board[1][turn2-4]==" ":
                    self.board[1][turn2-4]="O"
                else:
                    print("\nThat space is taken, please enter another number \n")
                    return self.player_2()
            else:
                if self.board[2][turn2-7]==" ":
                    self.board[2][turn2-7]="O"
                else:
                    print("\nThat space is taken, please enter another number \n")
                    return self.player_2()
        (self.print_board())


    def win(self):
       winner=False
       while winner==False:

           self.player_1()

           #checking for rows

           if self.board[0][0]=="X" and self.board[0][1]=="X" and self.board[0][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[1][0]=="X" and self.board[1][1]=="X" and self.board[1][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[2][0]=="X" and self.board[2][1]=="X" and self.board[2][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break
        


           #checking for columns
           elif self.board[0][0]=="X" and self.board[1][0]=="X" and self.board[2][0]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[0][1]=="X" and self.board[1][1]=="X" and self.board[2][1]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[0][2]=="X" and self.board[1][2]=="X" and self.board[2][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break


           #checking for diagonals
           elif self.board[0][0]=="X" and self.board[1][1]=="X" and self.board[2][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[0][2]=="X" and self.board[1][1]=="X" and self.board[2][0]=="X":
               print("congratulations, X wins!")
               winner=True
               break


            #now the same thing for O
           self.player_2()

           if self.board[0][0]=="O" and self.board[0][1]=="O" and self.board[0][2]=="O":
               print("congratulations, O wins!")
               winner=True
               break

           elif self.board[1][0]=="X" and self.board[1][1]=="X" and self.board[1][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[2][0]=="X" and self.board[2][1]=="X" and self.board[2][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break



           elif self.board[0][0]=="O" and self.board[1][0]=="O" and self.board[2][0]=="O":
               print("congratulations, O wins!")
               winner=True
               break

           elif self.board[0][1]=="X" and self.board[1][1]=="X" and self.board[2][1]=="X":
               print("congratulations, X wins!")
               winner=True
               break

           elif self.board[0][2]=="X" and self.board[1][2]=="X" and self.board[2][2]=="X":
               print("congratulations, X wins!")
               winner=True
               break



           elif self.board[0][0]=="O" and self.board[1][1]=="O" and self.board[2][2]=="O":
                print("congratulations, O wins!")
                winner=True
                break

           elif self.board[0][2]=="O" and self.board[1][1]=="O" and self.board[2][0]=="O":
                print("congratulations, O wins!")
                winner=True
                break
           else:
               pass










board1 = Board()
board1.print_board()
board1.win()
