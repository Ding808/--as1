import random
import array as arr

class First:
  def show(self):
    Hp = 5
    St = 0
    Dp = 0
    i = 1
    break0 = 0
    HP = 20
    ST = 2
    DP = 1
    while True:
      Hp *= 2
      St = St + 1
      Dp = Dp + 1
      I = arr.array('d', [HP, ST, DP])
      Monster = arr.array('d', [Hp, St, Dp])
      print(f"\033[93mThis monster's HP is: ",Monster[0],"\033[0m")
      print(f"\033[93mThis monster's ST is: ",Monster[1],"\033[0m")
      print(f"\033[93mThis monster's DP is: ",Monster[2],"\033[0m")
      print(f"\033[94mYour HP is: ",I[0],"\033[0m")
      print(f"\033[94mYour ST is: ",I[1],"\033[0m")
      print(f"\033[94mYour DP is: ",I[2],"\033[0m")
      while (Monster[0] > 0)&(I[0]>0):
        roll = input(f"\033[94mPlease type 'r' to roll the dice: \033[0m")
        print()
        if roll == "r":
          r = random.randint(1,6)
          print(f"\033[92mThe number you rolled is: ",r,"\033[0m")
          Monster[0] = Monster[0]-(r*I[1]-Monster[2])
          print(f"\033[95mYou successfully make ",r*I[1]-Monster[2]," damage to the monster\033[0m")
          print(f"\033[91mYour HP: ", I[0],"\033[0m")
          print(f"\033[91mMonster's HP: ",Monster[0],"\033[0m")
          if Monster[0] <= 0:
            print(f"\033[95mYou win!!!\033[0m")
            i = i+1
            HP = HP + 10
            ST = ST + 1
            DP = DP + 1
            next = input(f"\033[91mDo you want to go to the next level? \033[0m")
            if (next == "YES"):
              break
            elif(next == "NO"):
              print(f"\033[95mYou have no chance to leave LOL!!!\033[0m")
              break
            else:
              print(f"\033[95mYou have no chance to leave LOL!!!\033[0m")
              break
          r1 = random.randint(1,6)
          print(f"\033[92mThe number monster rolled is: ",r1,"\033[0m")
          I[0] = I[0] - (r1*Monster[1]-I[2])
          print(f"\033[95mMonster successfully make ",r1*Monster[1]-I[2]," damage to the you\033[0m")
          print(f"\033[91mYou HP: ", I[0],"\033[0m")
          print(f"\033[91mMonster's HP: ",Monster[0],"\033[0m")
          if I[0] <= 0:
            print(f"\033[96mMonster win!!! You lose!!!\033[0m")
            again = input(f"\033[96mDo you want to play again?\033[0m")
            if again == "YES":
              break0 = 0
              i = 1
              Hp = 5
              St = 0
              Dp = 0
              i = 1
              HP = 20
              ST = 2
              DP = 1
            else:
              break0 = 1
              break
      if (break0 == 1):
        print(f"\033[1mSee you when you are ready~ \033[0m")
        break
      if (i == 4):
        second = input("Do you want to move to the next round?")
        if second == "YES":
          Hp *= 1.5
          St *= 1.5
          Dp *= 1.5
          i = 1
          break0 = 0
        else:
          print(f"\033[1mSee you when you are ready~ \033[0m")
          break










