import sys,time,os

nazI = f"""\033[94m
        ░░░░░░░░░░░░░░░▄▀▄░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░▄▀░░░▀▄░░░░░░░░░░░░░
        ░░░░░░░░░░░▄▀░░░░▄▀█░░░░░░░░░░░░░
        ░░░░░░░░░▄▀░░░░▄▀░▄▀░▄▀▄░░░░░░░░░
        ░░░░░░░▄▀░░░░▄▀░▄▀░▄▀░░░▀▄░░░░░░░
        ░░░░░░░█▀▄░░░░▀█░▄▀░░░░░░░▀▄░░░░░
        ░░░▄▀▄░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░░░
        ░▄▀░░░▀▄░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░
        ░█▀▄░░░░▀▄░█▀░░░░░░░▀█░▀▄░▀▄░▄▀█░
        ░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░▀▄░█░▄▀░
        ░░░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░▀█▀░░░
        ░░░░░▀▄░▀▄░▄▀░▄▀░█▀░░░░▄▀█░░░░░░░
        ░░░░░░░▀▄░█░▄▀░▄▀░░░░▄▀░▄▀░░░░░░░
        ░░░░░░░░░▀█▀░▄▀░░░░▄▀░▄▀░░░░░░░░░
        ░░░░░░░░░░░░░█▀▄░▄▀░▄▀░░░░░░░░░░░
        ░░░░░░░░░░░░░▀▄░█░▄▀░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░▀█▀░░░░░░░░░░░░░░░\033[0m"""
sovieT = f"""\033[91m
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
            ░░░░░░░░░░▀▀▀██████▄▄▄░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░▀▀▀████▄░░░░░░░
            ░░░░░░░░░░▄███████▀░░░▀███▄░░░░░
            ░░░░░░░░▄███████▀░░░░░░░▀███▄░░░
            ░░░░░░▄████████░░░░░░░░░░░███▄░░
            ░░░░░██████████▄░░░░░░░░░░░███▌░
            ░░░░░▀█████▀░▀███▄░░░░░░░░░▐███░
            ░░░░░░░▀█▀░░░░░▀███▄░░░░░░░▐███░
            ░░░░░░░░░░░░░░░░░▀███▄░░░░░███▌░
            ░░░░▄██▄░░░░░░░░░░░▀███▄░░▐███░░
            ░░▄██████▄░░░░░░░░░░░▀███▄███░░░
            ░█████▀▀████▄▄░░░░░░░░▄█████░░░░
            ░████▀░░░▀▀█████▄▄▄▄█████████▄░░
            ░░▀▀░░░░░░░░░▀▀██████▀▀░░░▀▀██░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[0m"""
class sidebyside:
    def side(self):
        spacer = " " * 5  # Space between 
        for a, b in zip(nazI.splitlines(), sovieT.splitlines()):
            print(f'\033[94m{a}{spacer}\033[91m{b}\033[0m')
def texttime(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)

