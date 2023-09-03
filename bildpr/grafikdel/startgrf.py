from tqdm import tqdm
import time
from colorama import Fore, Back, Style

# Выполнение решения или компонента
print(Fore.GREEN + "\n")
while True:
    commandel = input(" <.DEL-Programms/grf: \n >>>  ")
    if commandel == "cd":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        break

    if commandel == "help":
        time.sleep(1)
        print(Fore.CYAN + "\n")
        print(" \n  Files.del        &/ File-PROG  \n ")
        print(" \n  Message          &/ MESSAGE.web    \n ")
        print(" \n  Змейка           &/ Змейка.games    \n ")
        print(" \n  Блокнот          &/ Text.sys  \n ")
        print(" \n  Назад в систему  &/ cd -l   \n ")
        print(Fore.YELLOW + "\n")

    if commandel == "File-PROG":
        time.sleep(1)
        from bildpr.grafikdel.bildgrf.Fileprog import *

    if commandel == "MESSAGE.web":
        time.sleep(1)
        from bildpr.grafikdel.bildgrf.Messagedel import *

    if commandel == "Змейка.games":
        time.sleep(1)
        from bildpr.grafikdel.bildgrf.Shakgame import *

    if commandel == "Text.sys":
        time.sleep(1)
        from bildpr.grafikdel.bildgrf.Textdelsu import *

    if commandel == "cd -l":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        print(Fore.RED + "\n ERROR SYS no if programms/grf on. \n   code sys integer 4553 \n conection sys ROOT off")
        print(Fore.YELLOW + "\n")
        break