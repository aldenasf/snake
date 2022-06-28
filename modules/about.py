import sys
from main import main
from modules import helper
from colorama import Fore as Color

sys.path.insert(0, "../")
enter_to_return = Color.RED + "[>] Press ENTER to return..."


def about():
    helper.about()
    print(Color.WHITE + "Developer:" + Color.CYAN + " AldenizenMC#1418")
    print(Color.WHITE + "Github:" + Color.CYAN + " https://github.com/AldenizenMC")
    print(Color.WHITE + "Version:" + Color.CYAN + " 1.0.0" + Color.RED)
    input(enter_to_return)
    helper.clear()
    return main()
