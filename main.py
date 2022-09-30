import random
import array as arr
class Main:
  def show(self): 
    n = 0
    for loop in range (0,4):
      start = input("Do you want to start the game?  Type 'YES' to start")
      if start == "YES":
        print("START")
        break
      elif (n == 3):
        print("DUMB")
        break
      else:
        n = n + 1

class First:
  def show(self):
    global Win
    HP = 20
    ST = 1
    DP = 0 #防御力
    I = arr.array('d', [HP, ST, DP])
    Hp = 20
    St = 1
    Dp = 0
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
        Win = True
      elif I[0] <= 0:
        print("Monster win!!! You lose!!!")
        print(Monster[0])
        Win = False
  def pass1 (self):
    return Win
      

class Second:
  def show(self):
    global Win
    HP = 20
    ST = 1
    DP = 0 #防御力
    I = arr.array('d', [HP, ST, DP])
    Hp = 30
    St = 1
    Dp = 0
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
        Win = True
      elif I[0] <= 0:
        print("Monster win!!! You lose!!!")
        print(Monster[0])
        Win = False
  def pass2 (self):
    return Win

class Third:
  def show(self):
    global Win
    HP = 20
    ST = 1
    DP = 0 #防御力
    I = arr.array('d', [HP, ST, DP])
    Hp = 40
    St = 1
    Dp = 0
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
        Win = True
      elif I[0] <= 0:
        print("Monster win!!! You lose!!!")
        print(Monster[0])
        Win = False
  def pass3 (self):
    return Win
    
    
         


        

      




