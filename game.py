#TASK 1: Hangman Game
#Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
#Simplified Scope:
# =>Use a small list of 5 predefined words (no need to use a file or API).
# =>Limit incorrect guesses to 6.
# =>Basic console input/output - no graphics or audio.
#ey Concepts Used: random, while loop, if-else, strings, lists.

import random as rd

def guess(d):
       word=''
       for i in range(0,len(d)):
              print("\nGuess the ",i+1," character")
              for j in range(0,6):
                     w=input("Chance "+str(j+1)+" : ").upper()
                     if d[i]==w:
                            print("\nCongragulate you guss correctly")
                            word=word+w
                            break
                     else:
                            print("You guessed wrong! Try again\n you have ",6-j,"chances\n")
              else:
                     print("\n\nSorry You failed!\nThe correct word is "+d)
                     print("You correctly guessed ",i," letters")
                     break
       if d==word:
              print("\n\nCongragulation you won\nThe correct word is",word)


def game_initiate():
       f=open("words.txt","r")
       c=f.readlines()
       f.close()
       d=rd.choice(c)
       d=d[:-1]
       guess(d)
       
def entry():
       while 1:
              print("\n\toptions\n\n1.play game\n2.Exit game\n")
              a=input("Enter option : ").lower()
              match a:
                     case 'play':
                            game_initiate()
                     case 'exit':
                            break
                     case _:
                            print("\nInvalid option\n")

if __name__=="__main__":
       entry()
