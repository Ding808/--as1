import random
import array as arr
import Nazi
import Soviet
import sys,time,os
from method import *
from os import system, name
from Nazi import *
from Soviet import *

a1 = Nazi.nazi()
b1 = Soviet.soviet()
#the clear method that can clear all the text
def clear():
  _ = system('clear')

class Start:
  def start(self):
    #Starting program to force player say yes
    n = 1
    #Beginning program
    for loop in range (0,3):
      start = input(f"\033[91m\033[1mDo you want to start the game?  Type 'YES' to start: \033[0m")
      if start == "YES":
        print(f"\033[92m\033[1mSTART!!!\033[0m")
        time.sleep(2)
        clear()
        break
      elif (n == 3):
        print(f"\033[91m\033[1mYou are so dumb, let me help you LOL\033[0m")
        print(f"\033[1m\033[1mYES\033[0m")
        time.sleep(2)
        clear()
        break
      else:
        n = n + 1  

class First:
  def show(self):
    #Hp, St and Dp is the init data of the monster
    Hp = 5
    St = 0
    Dp = 0
    #i counts the number of the game you played, if you win three times, it let you go to the next round
    i = 1
    #break0 is the breaker, if it equal to 1, it force to quit the game
    break0 = 0
    while True:
      role = input(f"\033[95m\033[1mDo you want to be 'Nazi' or 'Soviet' \033[0m").upper()
      if (role == "NAZI"):
        #HP, ST and DP change all the time to update the data from the game
        HP = initaHp
        ST = initaSt
        DP = initaDp
        slogan = input(f"\033[93m\033[1mWhat is your slogan? \033[0m").upper()
        break
      elif (role == "SOVIET"):
        slogan = input(f"\033[93m\033What is your slogan? \033[0m").upper()
        HP = initbHp
        ST = initbSt
        DP = initbDp
        break
      else:
        print("")
    while True:
      #Everytime the monster's data update to be stronger
      Hp *= 2
      St = St + 1
      Dp = Dp + 1
      #Make my data and monster data to an array
      I = arr.array('d', [HP, ST, DP])
      Monster = arr.array('d', [Hp, St, Dp])
      #When you say the wrong slogan of Nazi you lose
      if (slogan == "MY FUHRER")and(role == "NAZI"):
        texttime(a1.n())
        print("")
      elif (slogan == "YPA"):
        texttime(b1.s())
        print("")
      elif (slogan != "YPA")and(role == "SOVIET"):
        print(f"\033[94m\033[1mYPA!!!\033[0m")
        texttime(b1.s())
        print("")
      else:
        print(f"""\033[94m\033[1m
         _/卐\_ 
         (҂`_´)
         <,︻╦╤─ ҉ - -
         _/﹋\_\033[0m""")
        print("\033[91m\033[1mYou've be killed by the fuhrer. You lose\033[0m")
        break
      print(f"\033[93m\033[1mThe number of enemy are: ",Monster[0],"\033[0m")
      print(f"\033[93m\033[1mThe enemy's ST is: ",Monster[1],"\033[0m")
      print(f"\033[93m\033[1mThe enemy's DP is: ",Monster[2],"\033[0m")
      print(f"\033[94m\033[1mThe number of your soldiers are: ",I[0],"\033[0m")
      print(f"\033[94m\033[1mYour army's ST is: ",I[1],"\033[0m")
      print(f"\033[94m\033[1mYour army's DP is: ",I[2],"\033[0m")
      #end the game when monster or i die
      while (Monster[0] > 0)and(I[0]>0):
        roll = input(f"\033[94m\033[1mPlease type 'r' to roll the dice: \033[0m")
        print()
        #roll the dice to play random number
        if roll == "r":
          r = random.randint(1,6)
          print(f"\033[92m\033[1mThe number you rolled is: ",r,"\033[0m")
          Monster[0] = Monster[0]-(r*I[1]-Monster[2])
          print(f"\033[95m\033[1mYou successfully killed ",r*I[1]-Monster[2]," soldiers from enemy\033[0m")
          print(f"\033[91m\033[1mThe number of your soldiers are: ", I[0],"\033[0m")
          print(f"\033[91m\033[1mThe number of enemy's soldiers are: ",Monster[0],"\033[0m")
          if Monster[0] <= 0:
            if (role == "SOVIET"):
              print(f"""\033[91m\033[1m
                         _/☭☭\_ 
                         (҂`_´)
                         <,︻╦╤─ ҉ - -
                         _/﹋\_\033[0m""")
              print(b1.s())
              print("")
            elif (role == "NAZI"):
              print(f"""\033[94m\033[1m
                      _/卐\_ 
                      (҂`_´)
                      <,︻╦╤─ ҉ - -
                      _/﹋\_\033[0m""")
              print(a1.n())
              print("")
              print(f"\033[95m\033[1mYou win!!!\033[0m")
              i = i+1
              HP = HP + 10
              ST = ST + 1
              DP = DP + 1
              #you have to go to the next level when you win
            next = input(f"\033[91m\033[1mDo you want to go to the next level? (Yes/No) \033[0m").upper()
            if (next == "YES"):
              clear()
              break
            elif(next == "NO"):
              print(f"\033[95m\033[1mYou have no chance to leave LOL!!!\033[0m")
              time.sleep(2)
              clear()
              break
            else:
              print(f"\033[95m\033[1mYou have no chance to leave LOL!!!\033[0m")
              time.sleep(2)
              clear()
              break
          r1 = random.randint(1,6)
          print(f"\033[92m\033[1mThe number enemy rolled is: ",r1,"\033[0m")
          I[0] = I[0] - (r1*Monster[1]-I[2])
          print(f"\033[95m\033[1mThe enemy successfully killed ",r1*Monster[1]-I[2]," soldiers from your army\033[0m")
          print(f"\033[91m\033[1mYour number of the soldier are: ", I[0],"\033[0m")
          print(f"\033[91m\033[1mThe number of enemy's solders are: ",Monster[0],"\033[0m")
          if I[0] <= 0:
            if (role == "NAZI"):
              print(f"""\033[91m\033[1m
                       _/☭☭\_ 
                       (҂`_´)
                       <,︻╦╤─ ҉ - -
                       _/﹋\_\033[0m""")
              texttime(b1.s())
              print("")
            elif (role == "SOVIET"):
              print(f"""\033[94m\033[1m
                       _/卐\_ 
                       (҂`_´)
                       <,︻╦╤─ ҉ - -
                       _/﹋\_\033[0m""")
              texttime(a1.n())
              print("")
            print(f"\033[96m\033[1mThe enemy win!!! You lose!!!\033[0m")
            again = input(f"\033[96m\033[1mDo you want to play again? (Yes/No) \033[0m").upper()
            if again == "YES":
              #make data back to init number when you want to play again
              break0 = 0
              i = 1
              Hp = 5
              St = 0
              Dp = 0
              i = 1
              clear()
              role = input(f"\033[95m\033[1mDo you want to be 'Nazi' or 'Soviet' \033[0m").upper()
              slogan = input(f"\033[93m\033[1mWhat is your slogan? \033[0m").upper()
              if (role == "NAZI"):
                HP = initaHp
                ST = initaSt
                DP = initaDp
              elif (role == "SOVIET"):
                HP = initbHp
                ST = initbSt
                DP = initbDp
            else:
              break0 = 1
              break
      if (break0 == 1):
        #force to quit when break0 = 1
        print(f"\033[1m\033[1mSee you when you are ready~ \033[0m")
        break
      if (i == 4):
        second = input(f"\033[93m\033[1mDo you want to move to the next round? (Yes/No) \033[0m").upper()
        #next round's monster would be super strong
        if second == "YES":
          Hp *= 1.5
          St *= 1.5
          Dp *= 1.5
          i = 1
          break0 = 0
          clear()
          #Prize when you win the first round
          print(f"\033[92m\033[1mWOW, you successfully intercepted the souvenir from enemy!!! It's a model tank!!!\033[0m")
          texttime(f"""\033[96m
                ███████l▄▄▄▄▄▄▄▄▃  
            ▂▄▅█████████▅▄▃▂        
            l███████████████████]. 
            ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\033[0m""")
        else:
          print(f"\033[1m\033[1mSee you when you are ready~ \033[0m")
          break




