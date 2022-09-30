import main
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
test1 = main.First()
test2 = main.Second()
test3 = main.Third()

test1.show()
if (test1.pass1()==True):
    test2.show()
    if (test2.pass2()==True):
      test3.show()
      if (test3.pass3()==True):
        print("You win the whole game!!!")


