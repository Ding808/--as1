import Game
import sys,time,os
from method import *
import Game
import random
from PIL import Image

#Schlacht OF Сталинград
# Python3 -m pip install Pillow
#Using the Pillow to open the welcome image
img = Image.open('image.png')
img.show()
#Schlacht OF Сталинград

print(f"""\033[95m\033[1m         During the Sencond World War, Relations between the Nazis and the Soviet Union were getting worse. 
         Since July 17, 1942, Nazi and Soviet were having a war in Volgograd called 'the battle of Stalingrad. 
         In this game, you are going to play the role either Nazi or Soviet to win this war. Have fun ~ 
         And also, don't forgot your slogan of your army ~ Nazi: My fuhrer   Soviet: Ypa   \033[0m""")

#print two flag side by side
image = sidebyside()
image.side()

#Soviet's slogan is: YPA
#Nazi's slogan is: MY FÜHRER
test = Game.Start()
test.start()
#the main method of the game
test1 = Game.First()
test1.show()

