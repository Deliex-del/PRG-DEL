from tqdm import tqdm
import time
from colorama import Fore, Back, Style

# Выполнение решения или компонента
print(Fore.YELLOW + "\n")
while True:
    commandel = input(" <.DEL-Programms/: \n >>>  ")
    if commandel == "com":
        time.sleep(1)
        print(Fore.YELLOW + "\n")
        from bildpr.concoledel.startcom import *

    if commandel == "grf":
        time.sleep(1)
        print(Fore.YELLOW + "\n")
        from bildpr.grafikdel.startgrf import *

    if commandel == "msg":
        time.sleep(1)
        print(Fore.YELLOW + "\n")
        from bildpr.msgdel.startmsg import *

    if commandel == "help -l":
        time.sleep(1)
        print(Fore.CYAN + "\n")
        print(" \n  Console (Консольные программы. )   &/ com  \n ")
        print(" \n  GRF     (Графические программы.)   &/ grf  \n ")
        print(" \n  MSG DEL (Адаптивные программы. )   &/ msg  \n ")
        print(" \n  Назад   (Назад в систему.      )   &/ cd -l \n ")
        print(Fore.YELLOW + "\n")

    if commandel == "cd -l":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        print(Fore.RED + "\n ERROR SYS no if programms on. \n   code sys integer 4553 \n conection sys ROOT off")
        print(Fore.YELLOW + "\n")
        break