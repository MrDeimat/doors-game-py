from colorama import init, Fore
from colorama import Back
from colorama import Style
import time
from art import *

import random
mm = 0
hp = 3
bot = 0
player = 0


print('''
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣀⡠⠤⠴⠚⣿⠃
⠀⠸⣿⡭⣭⣿⣽⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⠓⠚⠉⣉⣀⣤⡤⣴⠀⣿⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢰⠞⢩⠀⢻⡏⠀⡏⠀⣿⠄
⠀⢠⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⠃⠀⣿⠂
⠀⢘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⡇⠀⣿⡇
⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⣷⠀⣿⡇
⠀⣠⣿⡇⠀Doors⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⣿⣼⣿⡇
⠀⡃⣿⡇⠀⠀Game⠀⠀⠀⠀⠀⢸⠀⠘⠛⠛⠒⠛⠓⠛⠛⣿⣿⡇
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢰⠦⢠⠀⢤⣤⣤⣄⠋⣿⡇
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠈⣿⠀⣿⡇
⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⣿⠀⣿⡇
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⣄⢸⠠⣼⡇⠀⣿⠀⣿⡇
⠀⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠉⠉⠀⠛⠚⠯⠿⠀⣿⡇
⠠⢿⣿⣷⣶⣶⣶⠶⢶⡶⢶⣶⣶⣶⣶⢿⣶⣤⣄⣀⣀⠀⠀⠀⢨⠀⣿⡇
⠀⠀⠀⠈⠀⠐⠒⠒⠀⠀⠀⠘⠁⠈⠀⠀⠀⠀⠉⠉⢛⠉⠑⠒⠠⠤⢿⠇
                             ''')


tprint('Doors Game')
print("Play - 1")
print("Exit - 2")
mm = int(input('Enter Number'))
if mm == 1:
    print('Loading...')
    time.sleep(0.3)
    print('Loading..')
    time.sleep(0.3)
    print('Loading.')
    time.sleep(0.3)
    print('Loading...')
    time.sleep(0.3)
    print('Loading..')
    time.sleep(0.3)
    print('Loading..')
    time.sleep(0.3)
    print('Loading.')
    time.sleep(0.3)
    print(Fore.GREEN + 'GO')
    print('round 1')
    print('1/2')
    player = int(input('choose door'))
    bot = random.randint(1,2)
    if player == bot:
        print('You Lost 1 HP')
        hp = hp =- 1
    else:
        print('round 2')
        print('1/2/3')
        player = int(input('choose door'))
        bot = random.randint(1, 2)
        if player == bot:
            print('You Lost 1 HP')
            hp = hp = - 1
        else:
            print('round 3')
            print('1/2/3')
            player = int(input('choose door'))
            bot = random.randint(1, 3)
            if player == bot:
                print('You Lost 1 HP')
                hp = hp = - 1
            else:
                print('round 4')
                print('1/2/3/4')
                player = int(input('choose door'))
                bot = random.randint(1, 4)
                
                if player == bot:
                    print('You Lost 1 HP')
                    hp = hp = - 1
                    

else:
    print('🗿')

