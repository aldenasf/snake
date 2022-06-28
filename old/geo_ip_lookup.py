import sys
import json
from modules import helper
import requests
import main as home
from colorama import Fore as Color
sys.path.insert(0, "../")

enter_to_return = Color.RED + "[>] Press ENTER to return..."


def main():
    ip = input("[>] IP Address: ")
    print("Gathering information...")
    ip_request = requests.get(f"http://ip-api.com/json/{ip}?fields=1098745")
    if ip_request.status_code == 200:
        ipdata = json.loads(ip_request.text)
        if ipdata["status"] == "success":
            print("⎯" * 50)
            print("[i] Continent: {}".format(ipdata["continent"]))
            print("[i] Region : {}".format(ipdata["regionName"]))
            print("[i] Country : {}".format(ipdata["country"]))
            print("[i] City : {}".format(ipdata["city"]))
            print("[i] Zip Code : {}".format(ipdata["zip"]))
            print("[i] Coordinates : {x}, {y}".format(x=ipdata["lon"], y=ipdata["lat"]))
            print("[i] Timezone: {}".format(ipdata["timezone"]))
            print("[i] ISP: {}".format(ipdata["isp"]))
            print("⎯" * 50)
            input(enter_to_return)
            helper.clear()
            main.main()
        elif ipdata["status"] == "fail":
            print("[!] Unable to gather information")
            input(enter_to_return)
            helper.clear()
            main.main()
    else:
        print(f"[!] Status code {ip_request.status_code}")
        input(enter_to_return)
        helper.clear()
        main.main()
