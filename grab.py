import requests, os, stdiomask
from uuid import uuid4
os.system('title  ')
os.system('cls||clear')
printf(" _           _                            _                               _               
(_)_ __  ___| |_ __ _   ___  ___  ___ ___(_) ___  _ __     __ _ _ __ __ _| |__   ___ _ __ 
| | '_ \/ __| __/ _` | / __|/ _ \/ __/ __| |/ _ \| '_ \   / _` | '__/ _` | '_ \ / _ \ '__|
| | | | \__ \ || (_| | \__ \  __/\__ \__ \ | (_) | | | | | (_| | | | (_| | |_) |  __/ |   
|_|_| |_|___/\__\__,_| |___/\___||___/___/_|\___/|_| |_|  \__, |_|  \__,_|_.__/ \___|_|   
                                                          |___/  github.com/keagtorb                       

")
print("")
username = input(f"[+] Enter Username: ")
password = stdiomask.getpass(f"[+] Enter Password: ")
headers = {

        "Host": "i.instagram.com",
        "X-Ig-Connection-Type": "WiFi",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Ig-Capabilities": "36r/Fx8=",
        "User-Agent": "Instagram 159.0.0.28.123 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 244425769) AppleWebKit/420+",
        "X-Ig-App-Locale": "en",
        "X-Mid": "Ypg64wAAAAGXLOPZjFPNikpr8nJt",
        "Content-Length": "778",
        "Accept-Encoding": "gzip, deflate"
        }
data = {

        "username":username,
        "reg_login":"0",
        "enc_password":f"#PWD_INSTAGRAM:0:&:{password}",
        "device_id":uuid4(),
        "login_attempt_count":"0",
        "phone_id":uuid4()
        }
url = "https://i.instagram.com/api/v1/accounts/login/"
r = requests.post(url=url,headers=headers,data=data)
session_id = r.cookies.get("sessionid")
if 'The password you entered is incorrect' in r.text:
 print(f"")
 print("")
 input(f"[+] wrong pass, enter 2 exit ")
 quit()
elif 'logged_in_user' in r.text:
 print(f"[+] Logged In Success")
else:
        print(r.text)
        input(f"Bad Login , Try Again")
        quit()
print(f"Session ID: {session_id}")
input("")
