import random
import array as arr

class First:
  def show(self):
    Hp = 20
    St = 1
    Dp = 0
    i = 1
    break0 = 0
    for guan in range (0,3):
      HP = 20
      ST = 1
      DP = 0
      Hp *= i
      St *= i
      Dp *= i
      I = arr.array('d', [HP, ST, DP])
      Monster = arr.array('d', [Hp, St, Dp])
      print(f"\033[93mThis monster's HP is: ",Hp,"\033[0m")
      print(f"\033[93mThis monster's ST is: ",St,"\033[0m")
      print(f"\033[93mThis monster's DP is: ",Dp,"\033[0m")
      while (Monster[0] > 0)&(I[0]>0):
        roll = input(f"\033[94mPlease type 'r' to roll the dice: \033[0m")
        print()
        if roll == "r":
          r = random.randint(1,6)
          print(f"\033[92mThe number you rolled is: ",r,"\033[0m")
          Monster[0] = Monster[0]-r
          print(f"\033[95mYou successfully make ",r," damage to the monster\033[0m")
          print(f"\033[91mYour HP: ", I[0],"\033[0m")
          print(f"\033[91mMonster's HP: ",Monster[0],"\033[0m")
          if Monster[0] <= 0:
            print(f"\033[95mYou win!!!\033[0m")
            i = i+1
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
          I[0] = I[0] - r1
          print(f"\033[95mMonster successfully make ",r1," damage to the you\033[0m")
          print(f"\033[91mYou HP: ", I[0],"\033[0m")
          print(f"\033[91mMonster's HP: ",Monster[0],"\033[0m")
          if I[0] <= 0:
            print(f"\033[96mMonster win!!! You lose!!!\033[0m")
            again = input(f"\033[96mDo you want to play again?\033[0m")
            if again == "YES":
              break0 = 0
              Hp = 20
              St = 1
              Dp = 0
              i = 1
            else:
              break0 = 1
              break
      if (break0 == 1):
        print(f"\033[1mSee you when you are ready~ \033[0m")
        break









