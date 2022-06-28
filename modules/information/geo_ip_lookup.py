import re
import sys
import requests
import json
from modules.helper import *

def get_ip():
        target = input("[>] IP Address: ")
        if not re.match(REGEX_IP, target):
            error("Invalid IP Address.", main)
        return target

def main():
    banner.geo_ip_lookup()
    print(" " * 15 + terminal.color + "0. All")
    print(" " * 15 + terminal.color + "1. Hackertarget.com")
    print(" " * 15 + terminal.color + "2. Ip-api.com")
    print(" " * 15 + terminal.color + "3. Ipapi.co")
    print(" " * 15 + terminal.color + "100. Return\n")
    option = input("[>] Option: ")
    if option == "":
        error(ERROR_UNSELECTED_OPTION, main)
    elif not option.isnumeric():
        error(ERROR_OPTION_NAN, main)
    elif int(option) == 0:
        t = get_ip()
        hackertarget(t, False)
        ip_api(t, False)
        ipapi(t, False)
        input("[>] Press ENTER to continue...")
        cls()
        main()
    elif int(option) == 1:
        hackertarget(get_ip())
    elif int(option) == 2:
        ip_api(get_ip())
    elif int(option) == 3:
        ipapi(get_ip())
    elif int(option) == 100:
        return
        # return
    else:
        error(ERROR_INVALID_OPTION, main)

def hackertarget(ip:str, goback:bool = True):
    if goback:
        print("[i] Fetching information...", end="\r")
    else:
        print("[i] [api.hackertarget.com] Fetching information...", end="\r")
    req = requests.get(f"https://api.hackertarget.com/geoip/?q={ip}")
    if req.status_code == 200:
        if not req.text == "error input invalid. enter IP address.":
            if goback:
                print("[i] Formatting json...", end="\r")
            else:
                print("[i] [api.hackertarget.com] Formatting json...", end="\r")
            data = {}
            for line in req.text.strip().splitlines(False): # Convert plain text to json
                key, value = line.split(":", 1)
                data[key.lower().replace(" ", "_")] = value.strip()
            print(" " * 50)
            print(terminal.color + "⎯" * 14 + "[ api.hacktarget.com ]" + "⎯" * 14)
            print(terminal.color + f"[i] IP Address  : " + terminal.value + data['ip_address'])
            print(terminal.color + f"[i] Country     : " + terminal.value + data['country'])
            print(terminal.color + f"[i] State       : " + terminal.value + data['state'])
            print(terminal.color + f"[i] City        : " + terminal.value + data['city'])
            print(terminal.color + f"[i] Latitude    : " + terminal.value + data['latitude'])
            print(terminal.color + f"[i] Longitude   : " + terminal.value + data['longitude'])
            print(terminal.color + "⎯" * 50 + "\n")
            if goback:
                input("Press ENTER to continue...")
                cls()
                main() 
            # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ api.hacktarget.com ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            # IP Address  : 1.1.1.1
            # Country     : Australia
            # State       :
            # City        :
            # Latitude    : -33.494
            # Longitude   : 143.2104
            # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        else:
            if goback:
                error("Invalid IP Address            ", main)
            else:
                print("[!] [api.hackertarget.com] Invalid IP Address")
    else:
        if goback:
            error(f"Unable to get information from api.hackertarget.com (Status Code {req.status_code})", main)
        else:
            print(f"[!] [api.hackertarget.com] Status Code {req.status_code}")

def ip_api(ip:str, goback:bool = True):
    if goback:
        print("[i] Fetching information...", end="\r")
    else:
        print("[i] [ip.api.com] Fetching information...", end="\r")
    req = requests.get(f"http://ip-api.com/json/{ip}?fields=26997753")
    if req.status_code == 200:
        data = json.loads(req.text)
        if data["status"] == "success":
            print(" " * 40)
            print(terminal.color + "⎯" * 18 + "[ ip-api.com ]" + "⎯" * 18)
            print(terminal.color + f"[i] Query       : " + terminal.value + str(data['query']))
            print(terminal.color + f"[i] Continent   : " + terminal.value + str(data['continent']))
            print(terminal.color + f"[i] Country     : " + terminal.value + str(data['country']))
            print(terminal.color + f"[i] Region      : " + terminal.value + str(data['regionName']))
            print(terminal.color + f"[i] City        : " + terminal.value + str(data['city']))
            print(terminal.color + f"[i] District    : " + terminal.value + str(data['district']))
            print(terminal.color + f"[i] Zip         : " + terminal.value + str(data['zip']))
            print(terminal.color + f"[i] Latitude    : " + terminal.value + str(data['lat']))
            print(terminal.color + f"[i] Longitude   : " + terminal.value + str(data['lon']))
            print(terminal.color + f"[i] Tmiezone    : " + terminal.value + str(data['timezone']))
            print(terminal.color + f"[i] Currency    : " + terminal.value + str(data['currency']))
            print(terminal.color + f"[i] ISP         : " + terminal.value + str(data['isp']))
            print(terminal.color + f"[i] Reverse     : " + terminal.value + str(data['reverse']))
            print(terminal.color + f"[i] Mobile      : " + terminal.value + str(data['mobile']).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
            print(terminal.color + f"[i] Proxy       : " + terminal.value + str(data['proxy']).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
            print(terminal.color + f"[i] Hosting     : " + terminal.value + str(data['hosting']).replace("True", terminal.true + "True").replace("False", terminal.false + "False"))
            print(terminal.color + "⎯" * 51 + "\n")
            # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ ip-api.com ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            # [i] Query       : 1.1.1.1
            # [i] Continent   : Oceania
            # [i] Country     : Australia
            # [i] Region      : Queensland
            # [i] City        : South Brisbane
            # [i] District    :
            # [i] Zip         : 4101
            # [i] Latitude    : -27.4766
            # [i] Longitude   : 153.0166
            # [i] Tmiezone    : Australia/Brisbane
            # [i] Currency    : AUD
            # [i] ISP         : Cloudflare, Inc
            # [i] Reverse     : one.one.one.one
            # [i] Mobile      : False
            # [i] Proxy       : False
            # [i] Hosting     : True
            # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            if goback:
                input("[>] Press ENTER to return...")
                cls()
                main()
        elif data["status"] == "fail":
            if goback:
                error("Unable to fetch information", main)
            else:
                print("[!] [ip-api.com] Unable to fetch information")
    else:
        if goback:
            error(f"Unable to get information from ip-api.com (Status Code {req.status_code})", main)
        else:
            print(f"[!] [ip-api.com] Status Code {req.status_code}")

def ipapi(ip:str, goback:bool = True):
    if goback:
        print("[i] Fetching information...", end="\r")
    else:
        print("[i] [ipapi.co] Fetching information...", end="\r")
    req = requests.get(f"https://ipapi.co/{ip}/json/")
    if req.status_code == 200:
        data = req.json()
        try:
            if data['error']:
                if goback:
                    error("Invalid IP Address.", main)
                else:
                    print("[!] [ipapi.co] Invalid IP Address")
                    return
        except KeyError:
            pass
        print(" " * 38)
        print(terminal.color + "⎯" * 19 + "[ ipapi.co ]" + "⎯" * 19)
        print(terminal.color + "[i] IP               : " + terminal.value + str(data['ip']))
        print(terminal.color + "[i] Version          : " + terminal.value + str(data['version']))
        print(terminal.color + "[i] City             : " + terminal.value + str(data['city']))
        print(terminal.color + "[i] Region           : " + terminal.value + str(data['region']))
        print(terminal.color + "[i] Country          : " + terminal.value + str(data['country_name']))
        print(terminal.color + "[i] Capital          : " + terminal.value + str(data['country_capital']))
        print(terminal.color + "[i] Postal           : " + terminal.value + str(data['postal']))
        print(terminal.color + "[i] Latitude         : " + terminal.value + str(data['latitude']))
        print(terminal.color + "[i] Longitude        : " + terminal.value + str(data['longitude']))
        print(terminal.color + "[i] Timezone         : " + terminal.value + str(data['timezone']))
        print(terminal.color + "[i] Calling Code     : " + terminal.value + str(data['country_calling_code']))
        print(terminal.color + "[i] Currency         : " + terminal.value + str(data['currency']))
        print(terminal.color + "[i] Languages        : " + terminal.value + str(data['languages']))
        print(terminal.color + "[i] Population       : " + terminal.value + str(data['country_population']))
        print(terminal.color + "⎯" * 50)
        if goback:
            input("[>] Press ENTER to continue...")
            cls()
            main()
        # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[ ipapi.co ]⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        # [i] IP               : 1.1.1.1
        # [i] Version          : IPv4
        # [i] City             : Sydney
        # [i] Region           : New South Wales
        # [i] Country          : Australia
        # [i] Capital          : Canberra
        # [i] Postal           : 2000
        # [i] Latitude         : -33.859336
        # [i] Longitude        : 151.203624
        # [i] Timezone         : Australia/Sydney
        # [i] Calling Code     : +61
        # [i] Currency         : AUD
        # [i] Languages        : en-AU
        # [i] Population       : 24992369
        # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        
    else:
        if goback:
            error(f"Unable to get information from ipapi.co (Status Code {req.status_code})", main)
        else:
            print(f"[!] [ipapi.co] Status Code {req.status_code})")

if __name__ == '__main__':
    main()