import sys
from colorama import Fore as Color
sys.path.insert(0, "..\\..\\")
from modules.information import geo_ip_lookup, port_scanner
from modules.attacks import dos, email_bomber
from modules.discord import nuker
from modules.helper import * #banner, error, ERROR_OPTION_NAN, ERROR_INVALID_OPTION, ERROR_UNSELECTED_OPTION, cls, terminal

# Main function
def main():
    opts = {
        "1": information_gatehring,
        "2": attacks,
        "3": discord
    }
    banner.main.main()
    print(" " * 15 + terminal.color + "1. Information gathering")
    print(" " * 15 + terminal.color + "2. Attacks")
    print(" " * 15 + terminal.color + "3. Discord")
    print(" " * 15 + terminal.color + "4. Email Bomber")
    print(" " * 15 + terminal.color + "99. Configuration")
    print(" " * 15 + terminal.color + "100. Exit\n")
    option = input("[>] Option:  ")
    if option == "100": 
        cls()
        print("[i] Exiting..." + Color.RESET)
        sys.exit()
    call = opts.get(str(option), invalid_option)
    cls()
    call()
    cls()
    main()

def settings():
    banner.main.settings()
    print(" " * 15 + Color.RED + "1. Hide IP Addresses: " + str(terminal.hide_ip_address).replace("True", Color.GREEN + "True").replace("False", Color.RED + "False"))
    print(" " * 15 + Color.RED + "100. Return\n")
    option = input("[>] Option: ")
    if option == "":
        error(ERROR_UNSELECTED_OPTION, settings)
    elif not option.isnumeric():
        error(ERROR_OPTION_NAN, settings)
    elif int(option) == 1:
        terminal.hide_ip_address = not terminal.hide_ip_address
        cls()
        settings()
    elif int(option) == 100:
        cls()
        main()
    else:
        error(ERROR_INVALID_OPTION, settings)

def information_gatehring():
    opts = {
        "1": port_scanner.main,
        "2": geo_ip_lookup.main,
        "100": main
    }
    banner.main.info()
    print(" " * 15 + terminal.color + "1. Port Scanner")
    print(" " * 15 + terminal.color + "2. GeoIP Lookup")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    call = opts.get(str(option), invalid_option_info)
    cls()
    call()
    cls()
    information_gatehring()

def attacks():
    opts = {
        "1": dos.main,
        "2": email_bomber.email_bomber,
        "100": main
    }
    banner.main.attacks()
    print(" " * 15 + terminal.color + "1. Denial of Service")
    print(" " * 15 + terminal.color + "2. Email Bomber")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    if option == "100":
        cls()
        main()
    call = opts.get(str(option), invalid_option_attacks)
    cls()
    call()
    cls()
    attacks()

def discord():
    opts = {
        "1": nuker.main
    }
    banner.discord.main()
    print(" " * 15 + terminal.color + "1. Nuker")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    if option == "100": 
        cls()
        main()
    call = opts.get(str(option))
    cls()
    call()
    cls()
    discord()
    

def invalid_option():
    error(ERROR_INVALID_OPTION, main)

def invalid_option_info():
    error(ERROR_INVALID_OPTION, information_gatehring)

def invalid_option_attacks():
    error(ERROR_INVALID_OPTION, attacks)

if __name__ == "__main__": main()
