import random
import array as arr
import Nazi
import Soviet
import sys,time,os
from tss import *

a1 = Nazi.nazi()
b1 = Soviet.soviet()
class Start:
  def start(self):
    #Starting program to force player say yes
    n = 1
    for loop in range (0,3):
      start = input(f"\033[91mDo you want to start the game?  Type 'YES' to start: \033[0m")
      if start == "YES":
        print("START!!!")
        break
      elif (n == 3):
        print(f"\033[91mYou are so dumb, let me help you LOL\033[0m")
        print(f"\033[1mYES\033[0m")
        break
      else:
        n = n + 1  

class First:
  def show(self):
    #make the init number of HP ST and DP
    global initaHp
    initaHp = 5
    initaSt = 2
    initaDp = 1
    initbHp = 15
    initbSt = 1
    initbDp = 2
    #Hp, St and Dp is the init data of the monster
    Hp = 5
    St = 0
    Dp = 0
    #i counts the number of the game you played, if you win three times, it let you go to the next round
    i = 1
    #break0 is the breaker, if it equal to 1, it force to quit the game
    break0 = 0
    while True:
      role = input(f"\033[95mDo you want to be 'Nazi' or 'Soviet' \033[0m").upper()
      if (role == "NAZI"):
        #HP, ST and DP change all the time to update the data from the game
        HP = initaHp
        ST = initaSt
        DP = initaDp
        slogan = input("What is your slogan? ").upper()
        break
      elif (role == "SOVIET"):
        slogan = input("What is your slogan? ").upper()
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
      if (slogan == "MY FUHRER")and(role == "NAZI"):
        texttime(a1.n())
        print("")
      elif (slogan == "YPA"):
        texttime(b1.s())
        print("")
      elif (slogan != "YPA")and(role == "SOVIET"):
        print("YPA!!!")
        texttime(b1.s())
        print("")
      else:
        print("""
         _/卐\_ 
         (҂`_´)
         <,︻╦╤─ ҉ - -
         _/﹋\_""")
        print("You've be killed by the fuhrer. You lose")
        break
      print(f"\033[93mThe number of enemy are: ",Monster[0],"\033[0m")
      print(f"\033[93mThe enemy's ST is: ",Monster[1],"\033[0m")
      print(f"\033[93mThe enemy's DP is: ",Monster[2],"\033[0m")
      print(f"\033[94mThe number of your soldiers are: ",I[0],"\033[0m")
      print(f"\033[94mYour army's ST is: ",I[1],"\033[0m")
      print(f"\033[94mYour army's DP is: ",I[2],"\033[0m")
      #end the game when monster or i die
      while (Monster[0] > 0)and(I[0]>0):
        roll = input(f"\033[94mPlease type 'r' to roll the dice: \033[0m")
        print()
        #roll the dice to play random number
        if roll == "r":
          r = random.randint(1,6)
          print(f"\033[92mThe number you rolled is: ",r,"\033[0m")
          Monster[0] = Monster[0]-(r*I[1]-Monster[2])
          print(f"\033[95mYou successfully killed ",r*I[1]-Monster[2]," soldiers from enemy\033[0m")
          print(f"\033[91mThe number of your soldiers are: ", I[0],"\033[0m")
          print(f"\033[91mThe number of enemy's soldiers are: ",Monster[0],"\033[0m")
          if Monster[0] <= 0:
            if (role == "SOVIET"):
              print("""
                         _/☭☭\_ 
                         (҂`_´)
                         <,︻╦╤─ ҉ - -
                         _/﹋\_""")
              print(b1.s())
              print("")
            elif (role == "NAZI"):
              print("""
                      _/卐\_ 
                      (҂`_´)
                      <,︻╦╤─ ҉ - -
                      _/﹋\_""")
              print(a1.n())
              print("")
              print(f"\033[95mYou win!!!\033[0m")
              i = i+1
              HP = HP + 10
              ST = ST + 1
              DP = DP + 1
              #you have to go to the next level when you win
            next = input(f"\033[91mDo you want to go to the next level? \033[0m").upper()
            if (next == "YES"):
              break
            elif(next == "NO"):
              print(f"\033[95mYou have no chance to leave LOL!!!\033[0m")
              break
            else:
              print(f"\033[95mYou have no chance to leave LOL!!!\033[0m")
              break
          r1 = random.randint(1,6)
          print(f"\033[92mThe number enemy rolled is: ",r1,"\033[0m")
          I[0] = I[0] - (r1*Monster[1]-I[2])
          print(f"\033[95mThe enemy successfully killed ",r1*Monster[1]-I[2]," soldiers from your army\033[0m")
          print(f"\033[91mYour number of the soldier are: ", I[0],"\033[0m")
          print(f"\033[91mThe number of enemy's solders are: ",Monster[0],"\033[0m")
          if I[0] <= 0:
            if (role == "NAZI"):
              print("""
                       _/☭☭\_ 
                       (҂`_´)
                       <,︻╦╤─ ҉ - -
                       _/﹋\_""")
              texttime(b1.s())
              print("")
            elif (role == "SOVIET"):
              print("""
                       _/卐\_ 
                       (҂`_´)
                       <,︻╦╤─ ҉ - -
                       _/﹋\_""")
              texttime(a1.n())
              print("")
            print(f"\033[96mThe enemy win!!! You lose!!!\033[0m")
            again = input(f"\033[96mDo you want to play again? \033[0m").upper()
            if again == "YES":
              #make data back to init number when you want to play again
              break0 = 0
              i = 1
              Hp = 5
              St = 0
              Dp = 0
              i = 1
              role = input(f"\033[95mDo you want to be 'Nazi' or 'Soviet' \033[0m").upper()
              slogan = input("What is your slogan? ").upper()
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
        print(f"\033[1mSee you when you are ready~ \033[0m")
        break
      if (i == 4):
        second = input(f"\033[93mDo you want to move to the next round?\033[0m").upper()
        #next round's monster would be super strong
        if second == "YES":
          Hp *= 1.5
          St *= 1.5
          Dp *= 1.5
          i = 1
          break0 = 0
          print("WOW, you successfully intercepted the souvenir from enemy!!! It's a model tank!!!")
          texttime(f"""\033[96m
                ███████l▄▄▄▄▄▄▄▄▃  
            ▂▄▅█████████▅▄▃▂        
            l███████████████████]. 
            ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\033[0m""")
        else:
          print(f"\033[1mSee you when you are ready~ \033[0m")
          break


#Ypa
#führer





