from tqdm import tqdm
import time
from colorama import Fore, Back, Style

# Выполнение решения или компонента
print(Fore.GREEN + "\n")
while True:
    commandel = input(" <.DEL-Programms/com: \n >>>  ")
    if commandel == "cd":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        break

    if commandel == "help":
        time.sleep(1)
        print(Fore.CYAN + "\n")
        print(" \n  BECDORdel        &/ BECDOR  \n ")
        print(" \n  DDOS.del         &/ DDOS    \n ")
        print(" \n  DEOS.del         &/ DEOS    \n ")
        print(" \n  IP-add.del       &/ IP-add  \n ")
        print(" \n  Назад в систему  &/ cd -l   \n ")
        print(Fore.YELLOW + "\n")

    if commandel == "BECDOR":
        time.sleep(1)
        from bildpr.concoledel.bildcom.BECDORdel import *

    if commandel == "DDOS":
        time.sleep(1)
        from bildpr.concoledel.bildcom.Ddosdel import *

    if commandel == "DEOS":
        time.sleep(1)
        from bildpr.concoledel.bildcom.DEOS import *

    if commandel == "IP-add":
        time.sleep(1)
        from bildpr.concoledel.bildcom.IPadd import *

    if commandel == "cd -l":
        print(Fore.YELLOW + "\n Вы перейдёте в начальный католог. \n")
        input()
        print(Fore.RED + "\n ERROR SYS no if programms/com on. \n   code sys integer 4553 \n conection sys ROOT off")
        print(Fore.YELLOW + "\n")
        break