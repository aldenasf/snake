import sys
from modules import helper
import socket
import logging
import main as home
from datetime import datetime
from colorama import Fore as Color
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "../")

enter_to_return = Color.RED + "[>] Press ENTER to return..."


def main():
    helper.port_scanner()
    print(" " * 15 + "1 - Single port")
    print(" " * 15 + "2 - Multiple ports")
    print(" " * 15 + "100 - Return")
    i = int(input(f"\n\n[>] Enter: "))
    if i == "":
        helper.cls()
        print("[!] Choose an option.")
        return main()
    elif int(i) == 1:
        port_scanner_single()
    elif int(i) == 2:
        port_scanner_multiple_opt()
    elif int(i) == 100:
        helper.cls()
        home.main()
    else:
        helper.cls()
        print("[!] Invalid option.")
        return main()


def port_scanner_single():
    target = str(input("[>] Target IP: "))
    port = int(input("[>] Port: "))
    scan_port(target=target, port=port, debug=False)
    input(enter_to_return)
    helper.cls()
    main()


def port_scanner_multiple_opt():
    helper.cls()
    helper.main()
    print(" " * 15 + "1 - Scan all ports (1-65535)")
    print(" " * 15 + "2 - Scan port in range")
    print(" " * 15 + "100 - Return")
    i = int(input("\n\n[>] Enter: "))
    if i == "":
        helper.cls()
        print("[!] Choose an option.")
        return port_scanner_multiple_opt()
    elif int(i) == 1:
        port_scanner_all()
    elif int(i) == 2:
        port_scanner_multiple()
    elif int(i) == 100:
        helper.cls()
        return main()


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
        input(enter_to_return)
        helper.cls()
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
        input(enter_to_return)
        helper.cls()
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
        s.close()
    except KeyboardInterrupt:
        print(Color.RED + "[!] Exiting port scanner..")
        helper.cls()
        return main()
    except socket.error:
        helper.cls()
        print(Color.RED + "[!] Host is not responding :(")
        input(enter_to_return)
        helper.cls()
