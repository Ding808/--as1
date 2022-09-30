import random
import array as arr

class First:
  def show(self):
    global Win
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
      while (Monster[0] > 0)&(I[0]>0):
        r = random.randint(1,6)
        Monster[0] = Monster[0]-r
        print("I", I[0], r)
        r1 = random.randint(1,6)
        I[0] = I[0] - r1
        print("M",Monster[0], r1)
        if Monster[0] <= 0:
          print("Human win!!!")
          print(I[0])
          i = i+1
          next = input("Do you want to go to the next level? ")
          if (next == "YES"):
            break
          elif(next == "NO"):
            print("You have no chance to leave LOL!!!")
            break
          else:
            print("You have no chance to leave LOL!!!")
            break
        elif I[0] <= 0:
          print("Monster win!!! You lose!!!")
          print(Monster[0])
          break0 = 1
          break
      if (break0 == 1):
        break



