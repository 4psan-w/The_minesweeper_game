import numpy as np
import random as r
from time import sleep
from itertools import product
from playsound import playsound
import sys
import time
import keyboard


def blinks(text, blink_count=5, blink_speed=1):
    for _ in range(blink_count):
        # Display the text
        sys.stdout.write(f'\r{text}')
        sys.stdout.flush()
        time.sleep(blink_speed)
        
        # Clear the text
        sys.stdout.write('\r' + ' ' * len(text))
        sys.stdout.flush()
        time.sleep(blink_speed)

class minesweeper:
    # necessary Variables such as player name and scores that are used the entire game 
    
    playername=""
    score = 0
    level_completion = 0
    
    
    # Function to increase the level according to the previous oneS ;
    def level_two(self):
        pass
    def won(self):
        if(self.level_completion == 1):
            self.level_two()
    
    
    
    # Starts the game 
    def start(self):
        self.playername = input("What's your name Mr. self?\n>")
        if(self.playername == ""):
            self.playername = "Player"
        print("THE MINESWEEEPER GAME")
    
    
    
    # Nothing Rocket science but A simple Game introductor
    def introduction(self):
        print("*************************************************************")
        print(f"Welcome to the Ultimate Minesweeper game Mr.{self.playername}")
        print("*************************************************************")
        print()
        print()
        blinks(f"Let me Introduce to some rules or introduce you about the game first if you want me to. (y/n)?")
        print()
        intr=input(">>")
        if(intr.capitalize() == 'Y' ):
            define = ".... So this game is called minesweeper as inside the tiles there lies few or a single mine so the objective of the game is to make it through all the tiles without stepping on them"
            levels = ".... This game has levels stacked after the completion of level 1 you will be directed to the second level and to the third"
            third = "..... The third level of this game is the most hardest and after the completion of the level is the completion of the game"
            final = f"...So BRACE THE HELL UP MR. {(self.playername).capitalize()} WE ARE GOING MINE HUNTING BEST OF LUCK....."
            
            # print("press Enter to skip...")
            for letters in define:
                print(letters ,end="")
                sleep(0.04)
            
            print()
            print()
            for letters in levels:
                print(letters , end="")
                sleep(0.04)
            print()
            print()
            for letters in third:
                print(letters ,end="")
                sleep(0.04)
            print()
            print()
            for letters in final:
                print(letters , end="")
                sleep(0.1)
            print()
            print("*" * 104)
        else:
            pass
        
    # determines the winning grid i.e   TOTAL GRIDS - GRIDS CONTAINING MINES
    def wingrids(self,total,mine):
        for elements in mine:
            if(elements in total):
                total.remove(elements)
        return total
        
    
    
    # checks if the user has pressed every tiles except for the ones with the mines underneath 
    # And if All the tiles are pressed without pressing onto the mines it returns true else False and game continues
    def checks(self,win_grids,tries):
        # total_grids = [i for i in range(10)]
        # mine_grids = [r.randint(0,10),r.randint(0,10),r.randint(0,10)]
        # win_grids = self.wingrids(total_grids,mine_grids)
        ifwon = False
        for elements in win_grids:
            if elements in tries:
                ifwon = True
            else:
                ifwon = False
                return False
        return ifwon
    




    # LEVEL ONE FOR THE GAME
    def game(self):
        grid_ord = list(product( [i for i in range(0,5)],[i for i in range(0,5)]))
        grid = np.array([["#","#","#","#","#"],
                         ["#","#","#","#","#"],
                         ["#","#","#","#","#"],
                         ["#","#","#","#","#"],
                         ["#","#","#","#","#"]])
        
        # print(grid_ord)         
        game_over = False
        tries = []
        inc = 10
        univ =[]
        for elements in product([i for i in range(0,5)],[i for i in range(0,5)]):
            univ.append(elements)
        mine_is_in = [(r.randint(0,2),r.randint(0,2)),
                        (r.randint(0,2),r.randint(0,2)),
                        [r.randint(0,4),r.randint(0,4)],
                        [r.randint(0,4),r.randint(0,4)],
                        [r.randint(0,4),r.randint(0,4)],
                        (r.randint(0,2),r.randint(0,2))]
        win_grids = self.wingrids(grid_ord,mine_is_in)
        # print(win_grids)
        while(not game_over):
            print(grid)
            if(tries != []):
                print(f"Your Tries :               {tries}")
            # print(mine_is_in)
            
            # print(f" the mines are in : {mine_is_in}")
            
            print("BE CAREFUL DONOT STEP ON THE MINE !! ")
            print()
            print()
            
            print("__"*20)
            print("Enter the order where you dont Think the mine is ")

            row = int(input("Row    >"))
            column = int(input("column      >"))
            user = row,column
            

            if(user in tries):
                print("TRIED ALREADY")
                print()
                print()
                print(f":: tried {tries} ::")
                print()
                print()
                continue            
            if(tuple(user) in mine_is_in):
                game_over= True
                playsound("/media/apsync/Codes/mini_projects/the Minesweeper/explosion-42132.wav")
                print("THE MINE EXPLODED YOU LOST")
                
                print("             "*2,f"Your score is {self.score}")            
                continue
            else:
                # playsound("/media/apsync/Codes/mini_projects/the Minesweeper/yay_z.wav")
                print("Close One")
                print("again")
                grid[row,column]="X"
                self.score = self.score + inc
                inc = inc + 3
                tries.append((user))
                print("             "*2,f"Your score is {self.score}")
                if_won = self.checks(win_grids, tries)
            
                if(if_won):
                    print("CONGRATULATIONS YOU WON")
                    self.won()
                    self.level_completion += 1
                    game_over = True
                    break

play = minesweeper()
# self = minesweeper()

# play.introduction()
play.game()
rounds_count  =0
while((input("Play Again (y/n) ? ")).lower() == "y"):
    rounds_count +=1
    print()
    print()
    print(f"** Rounds Count : : {rounds_count}")
    print()
    print()
    play.game()
