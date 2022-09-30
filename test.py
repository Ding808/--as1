import main
n = 0
for loop in range (0,4):
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
test1 = main.First()

test1.show()

# test1.show()
# if (test1.pass1()==True):
#     test2.show()
#     if (test2.pass2()==True):
#       test3.show()
#       if (test3.pass3()==True):
#         print("You win the whole game!!!")



