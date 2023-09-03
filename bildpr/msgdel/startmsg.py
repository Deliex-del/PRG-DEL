from tqdm import tqdm
import time
from colorama import Fore, Back, Style

# Выполнение решения или компонента
print(Fore.GREEN + "\n")
while True:
    commandel = input(" <.DEL-Programms/msg: \n >>>  ")
    if commandel == "cd":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        break

    if commandel == "help":
        time.sleep(1)
        print(Fore.CYAN + "\n")
        print(" \n  YADER.DEL        &/ YADER  \n ")
        print(" \n  WEB.DEL          &/ WEB    \n ")
        print(" \n  Назад в систему  &/ cd -l   \n ")
        print(Fore.YELLOW + "\n")

    if commandel == "YADER":
        time.sleep(1)
        from bildpr.msgdel.bildmsg.Yader import *

    if commandel == "WEB":
        time.sleep(1)
        from bildpr.msgdel.bildmsg.webdel.Server.Start.Startwebdel import *

    if commandel == "cd -l":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        print(Fore.RED + "\n ERROR SYS no if programms/msg on. \n   code sys integer 4553 \n conection sys ROOT off")
        print(Fore.YELLOW + "\n")
        break