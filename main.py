from Characters import characters
import random, sys, os
from sys import platform


def main():
    clear()
    menu()
    inGameMenu()
    fight()

def fight():
        orc = characters(100, 20)
        knight = characters(75,25)
        print('You met orc and you end up in fight')
        while orc.hp >= 0 or knight.hp >= 0:
            print('Press a to attack or e to escape')
            attackOrEscape = input()
            if attackOrEscape == 'a':
                orc.hp -= truncatedRngMultiplayer(2) * knight.attack
                print(f'You attack orc and he currently have {orc.hp}')
                knight.hp -= truncatedRngMultiplayer(2) * orc.attack
                print(f'Orc attack you and you currently have {knight.hp}')
            elif attackOrEscape == 'e':
                quit()
            else:
                print('Try again')
                continue

def menu():
    while True:
        print("Hello press p for play or e to exit")
        answer = input().lower()
        if answer == 'p':
            clear()
            break
        elif answer == 'e':
            sys.exit() # nefunguje
        else:
            print("Wrong key try again")
            continue

def inGameMenu():
    while True:
        print('Where you want to go you?')
        print("Press the number from the menu")
        print('1) Pub')
        print('2) Shop')
        print('3) Adventure')
        print('4) Exit game')
        option = int(input('Enter your choice: ')) 
        if option == 1:
            print('Pub - Nice option to heal yourself')
            break
        elif option == 2:
            print('Shop - Buy a sharper sword to chop more enemies')
            break
        elif option == 3:
            print('Adventure - Dont get killed')
            break
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
            continue        
    return option

def clear():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

def pub():
    pass

def rngFunction():
    rngMultiplayer = round(random.uniform(0.75, 1.25),2)
    return(rngMultiplayer)

def truncatedRngMultiplayer(rngMultiplayer, decimals = 0):
    multiplier = 10 ** decimals
    return int(rngMultiplayer * multiplier) / multiplier

if __name__ == "__main__":
    main()
