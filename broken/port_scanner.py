import sys
from modules.helper import *
import socket
import logging
import main as home
from datetime import datetime
from colorama import Fore as Color
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "../")
def main():
    banner.port_scanner()
    print(" " * 15 + "1 - Single port")
    print(" " * 15 + "2 - Multiple ports")
    print(" " * 15 + "100 - Return")
    i = int(input(f"\n\n[>] Enter: "))
    if i == "":
        error(ERROR_UNSELECTED_OPTION)
    elif int(i) == 1:
        cls()
        port_scanner_single()
    elif int(i) == 2:
        cls()
        port_scanner_multiple_opt()
    elif int(i) == 100:
        cls()
        home.main()
    else:
        error(ERROR_INVALID_OPTION, main)


def port_scanner_single():
    target = str(input("[>] Target IP: "))
    port = int(input("[>] Port: "))
    scan_port(target=target, port=port, debug=False)
    input(INPUT_ENTER)
    cls()
    main()


def port_scanner_multiple_opt():
    cls()
    banner.port_scanner()
    print(" " * 15 + "1 - Scan all ports (1-65535)")
    print(" " * 15 + "2 - Scan port in range")
    print(" " * 15 + "100 - Return")
    i = int(input("\n\n[>] Enter: "))
    if i == "":
        error(ERROR_UNSELECTED_OPTION)
    elif int(i) == 1:
        port_scanner_all()
    elif int(i) == 2:
        port_scanner_multiple()
    elif int(i) == 100:
        cls()
        return main()
    else:
        error(ERROR_INVALID_OPTION, port_scanner_multiple_opt)   


def port_scanner_multiple():
    debug = False
    target = str(input("[>] Target IP: "))
    range_from = int(input("[>] Start from port: "))
    range_to = int(input("[>] End on port: "))
    timeout = float(input("[>] Timeout (seconds): "))
    savelog = str(input("[>] Save result to a file? (Y/n)"))
    if savelog.lower() == "y" or savelog.lower() == "":
        debug = True
        logfile = str(input("[>] Save result as: "))
        logging.basicConfig(filename=logfile, format="%(message)s", level=logging.DEBUG)
    print("⎯" * 50)
    print(f"[i] Scanning target: {target}")
    print(f"[i] Scanning from port {range_from} to port {range_to}")
    print(f"[i] Scan timeout: {timeout}")
    if debug: print(f"[i] Scan result file: {logfile}")
    print(f"[i] Scanning started at: {datetime.now()}")
    print("⎯" * 50)
    socket.setdefaulttimeout(float(timeout))
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(range_from, range_to + 1):
            executor.submit(scan_port(target=target, port=port, debug=debug))
        if debug:
            print(Color.GREEN + "[i] Scan finished and saved to {}".format(logfile))
        else:
            print(Color.GREEN + "[i] Scan finished.")
        input("[>] Press ENTER to return...")
        cls()
        port_scanner_multiple_opt()


def port_scanner_all():
    debug = False
    target = str(input("[>] Target IP: "))
    timeout = float(input("[>] Timeout (seconds): "))
    savelog = str(input("[>] Save result to a file? (Y/n)"))
    if savelog.lower() == "y" or savelog.lower() == "":
        debug = True
        logfile = str(input("[>] Save result as: "))
        logfile = f"..\\{logfile}"
        logging.basicConfig(filename=logfile, format="%(message)s", level=logging.DEBUG)
    print("⎯" * 50)
    print(f"[i] Scanning target: {target}")
    print(f"[i] Scan timeout: {timeout}")
    if debug: print(f"[i] Scan result file: {logfile}")
    print(f"[i] Scanning started at: {datetime.now()}")
    print("⎯" * 50)
    socket.setdefaulttimeout(float(timeout))
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 65536):
            executor.submit(scan_port(target=target, port=port, debug=debug))
        if debug:
            print(Color.GREEN + "[i] Scan finished and saved to {}".format(logfile))
        else:
            print(Color.GREEN + "[i] Scan finished.")
        input("[>] Press ENTER to return...")
        cls()
        port_scanner_multiple_opt()


def scan_port(target, port, debug):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        if result == 0:
            print(Color.GREEN + f"[+] Port {port} is open")
            if bool(debug):
                logging.debug(f"Port {port} is open")
        else:
            print(Color.RED + f"[-] Port {port} is closed")
            if bool(debug):
                logging.debug(f"Port {port} is open")
    except KeyboardInterrupt:
        print(Color.RED + "[!] Exiting port scanner..")
        cls()
        return main()
    except socket.error:
        cls()
        print(Color.RED + "[!] Host is not responding :(")
        input("[>] Press ENTER to return...")
        cls()
