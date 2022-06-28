import json
import re
import sys
from queue import Queue
import socket
from threading import Thread
from modules.helper import *
# import main as home

class scanner:
    onetime = True
    target:str = '127.0.0.1'
    queue = Queue()
    open_ports = []
    threads = 1000
    hide_closed = True

def main():
    if scanner.onetime:
        scanner.onetime = False
        for i in range(1, 65536):
            scanner.queue.put(i)
    banner.port_scanner()
    print(" " * 15 + terminal.color + "1. Single port")
    print(" " * 15 + terminal.color + "2. Multiple port")
    print(" " * 15 + terminal.color + "100. Return\n")

    option = input("[>] Option: ")
    if option == "":
        error(ERROR_UNSELECTED_OPTION, main)
    elif not option.isnumeric():
        error(ERROR_OPTION_NAN, main)
    elif int(option) == 1:
        cls()
        single_scan()
    elif int(option) == 2:
        cls()
        multiple_scans()
    elif int(option) == 100:
        # cls()
        # sys.exit()
        # home.main()
        return
        # return
    else:
        error(ERROR_INVALID_OPTION, main)

def single_scan():
    banner.port_scanner()
    target = input("\n[>] IP Address: ")
    if not re.match(REGEX_IP, target):
        if not re.match(REGEX_DNS, target):
            error("Invalid IP Address", single_scan)
    scanner.target = target
    port = input("[>] Port: ")
    if not re.match(REGEX_PORT, port):
        error("Invalid port", single_scan)
    timeout = input("[>] Timeout (None): ")
    if not is_float(timeout) and not timeout == "":
        error("Timeout is not a number", single_scan)
    elif timeout == "":
        timeout = 0
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not float(timeout) <= 0:
            s.timeout = float(timeout)
        # print(f"[i] Connecting...",end="\r")
        result = scan(int(port))
        if result:
            print(terminal.true + "[i] Port {} is open.".format(port) + terminal.color)
        else:
            print(terminal.false  + "[i] Port {} is closed.".format(port) + terminal.color) 
        input("Press ENTER to return...")
        cls()
        main()
    except socket.error:
        error("Host is not responding", main)


def multiple_scans():
    banner.port_scanner()
    if re.match(REGEX_DNS, scanner.target):
        print(" " * 15 + terminal.color + "1. IP Address                 : " + terminal.value + str(scanner.target) + " (DNS)")
    else:
        print(" " * 15 + terminal.color + "1. IP Address                 : " + terminal.value + str(scanner.target))
    try:
        print(" " * 15 + terminal.color + "2. Ports                      : " + terminal.value + f"{scanner.queue.queue[0]}-{scanner.queue.queue[-1]}")
    except IndexError:
        if not scanner.queue.empty():
            with scanner.queue.mutex:
                scanner.queue.queue.clear()
            for port in range(1, 65536):
                scanner.queue.put(int(port))
            scanner.total_ports = int(len(scanner.queue.queue))
            cls()
            multiple_scans()
    print(" " * 15 + terminal.color + "3. Timeout                    : " + terminal.value + str(socket.getdefaulttimeout()))
    if scanner.threads >= 10000:
        print(" " * 15 + terminal.color + "4. Threads                    : " + terminal.value + str(scanner.threads) + " (Might freeze your PC)")
    else:
        print(" " * 15 + terminal.color + "4. Threads                    : " + terminal.value + str(scanner.threads))
    if not scanner.hide_closed:
        print(" " * 15 + terminal.color + "5. Hide closed ports          : " + terminal.value + str(scanner.hide_closed) + " (Ports will not show in order)")
    else:
        print(" " * 15 + terminal.color + "5. Hide closed ports          : " + terminal.value + str(scanner.hide_closed))
    print(" " * 15 + terminal.color + "99. Scan")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    if option == "":
        error(ERROR_UNSELECTED_OPTION, multiple_scans)
    elif not option.isnumeric():
        error(ERROR_OPTION_NAN, multiple_scans)
    elif int(option) == 1:
        ip = input("[>] IP Address: ")
        if not re.match(REGEX_IP, ip):
            if not re.match(REGEX_DNS, ip):
                error("[!] Invalid IP address.", multiple_scans)
            else:
                scanner.target = ip
                cls()
                multiple_scans()
        else:
            scanner.target = ip
            cls()
            multiple_scans()
    elif int(option) == 2:
        start_port = input("[>] Start from port: ")
        if not re.match(REGEX_PORT,start_port):
            error("[>] Invalid port.", multiple_scans)
        end_port = input("[>] Stop on port: ")
        if not re.match(REGEX_PORT, end_port):
            error("[>] Invalid port.", multiple_scans)
        elif end_port < start_port:
            error("[>] Ending port cannot be greater than starting port", multiple_scans)
        else:
            if not scanner.queue.empty():
                with scanner.queue.mutex:
                    scanner.queue.queue.clear()
            start_port = int(start_port)
            end_port = int(end_port)
            for port in range(start_port, end_port + 1):
                scanner.queue.put(int(port))
            scanner.total_ports = int(len(scanner.queue.queue))
            cls()
            multiple_scans()
    elif int(option) == 3:
        timeout = input("[>] Timeout: ")
        if timeout == "" or timeout == "0":
            socket.setdefaulttimeout(None)
            cls()
            multiple_scans()
        elif not is_float(timeout):
            error("Timeout is not a number", multiple_scans)
        else:
            socket.setdefaulttimeout(float(timeout))
            cls()
            multiple_scans()
    elif int(option) == 4:
        threads = input("[>] Threads: ")
        if threads == "":
            error("Thread cannot be empty.", multiple_scans)
        elif not threads.isnumeric():
            error("Thread is not a number.", multiple_scans)
        elif int(threads) >= 10000:
            confirm = input(f"[>] Are you sure you wanna use over 10k threads (Y/n)")
            if confirm.lower() == "y" or confirm == "":
                scanner.threads = int(threads)
                cls()
                multiple_scans()
            else:
                cls()
                multiple_scans()
        else:
            scanner.threads = int(threads)
            cls()
            multiple_scans()
    elif int(option) == 5:
        scanner.hide_closed = not scanner.hide_closed
        cls()
        multiple_scans()
    elif int(option) == 99:
        run_scanner(scanner.threads)
    elif int(option) == 100:
        cls()
        main()
    else:
        error(ERROR_INVALID_OPTION, multiple_scans)

def run_scanner(threads):
    thread_list = []

    for t in range(threads):
        thread = Thread(target=worker)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()
    
    if not len(scanner.open_ports) == 0:
        print(terminal.true + "[i] Finished with open ports : [ ", end="")
        for port in scanner.open_ports:
            print(terminal.value + f"'{port}' " + terminal.true, end="")
        print("]                                                \n" + terminal.color)
        multiple_scans()
    else:
        print(terminal.false + "[i] No open ports were found                                                " + terminal.color)
    
    input("[>] Press ENTER to return...")
    cls()
    main()

def worker():
    while not scanner.queue.empty():
        try:
            # print(f"{port} : {type(port)}")
            # input("")
            port = scanner.queue.get()
            current = scanner.queue.queue[0]
            max = scanner.queue.queue[-1]
            # percent = format((current / max) * 100, ".1f")
            percent = format(float_percentage(current, max), ".1f")
            print(f"[i] Scanning port {current}/{max} ({percent}%)  Open: {len(scanner.open_ports)}", end="\r")
            
            result = scan(int(port))
            
            if result:
                print(terminal.true + "[i] Port {} is open.                                       ".format(port) + terminal.color)
                scanner.open_ports.append(port)
            elif not scanner.hide_closed:
                print(terminal.false  + "[i] Port {} is closed.                                                ".format(port) + terminal.color) 
        except KeyboardInterrupt:
            cls()
            if not len(scanner.open_ports) == 0:
                print(terminal.true + "[i] Finished with open ports : [ ", end="")
                for port in scanner.open_ports:
                    print(terminal.value + f"'{port}' " + terminal.true, end="")
                print("]                                                \n" + terminal.color)
                multiple_scans()
            else:
                print(terminal.false + "[i] No open ports were found                                                " + terminal.color)
        except socket.error:
            error("Host is not responding                                                 ", multiple_scans)
        except IndexError:
            pass

def scan(port:int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect((scanner.target, port))
        return True
    except:
        return False

def scan2(port:int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((scanner.target, port))
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False

if __name__ == '__main__':
    main()

# Router
# [ '25' '53' '80' '110' '119' '143' '443' '465' '563' '587' '993' '995' '18991' ]