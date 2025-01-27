# Coded by @hadex4president
import requests, gratient
from os import system

system("cls && title Linkvertise Bypasser")

banner = (gratient.purple("""
 █    ▄█    ▄   █  █▀ ███ ▀▄    ▄ █ ▄▄  ██      ▄▄▄▄▄    ▄▄▄▄▄   ▄███▄   █▄▄▄▄
 █    ██     █  █▄█   █  █  █  █  █   █ █ █    █     ▀▄ █     ▀▄ █▀   ▀  █  ▄▀
 █    ██ ██   █ █▀▄   █ ▀ ▄  ▀█   █▀▀▀  █▄▄█ ▄  ▀▀▀▀▄ ▄  ▀▀▀▀▄   ██▄▄    █▀▀▌
 ███▄ ▐█ █ █  █ █  █  █  ▄▀  █    █     █  █  ▀▄▄▄▄▀   ▀▄▄▄▄▀    █▄   ▄▀ █  █
     ▀ ▐ █  █ █   █   ███  ▄▀      █       █                     ▀███▀     █
         █   ██  ▀                  ▀     █    v             x            ▀
                                         ▀        e   n   a
"""))

def purple(text):
    system(""); faded = ""
    red = 35
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}")
    return faded

def red(text):
    system(""); faded = ""
    green = 250
    for character in text:
        green -= 5
        if green < 0:
            green = 0
        faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
    return faded

print(banner)
link = input(purple(" ==> Dein Link : "))

headers = {
"Host": "bypass.bot.nu",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://bypass.bot.nu/",
"Connection": "keep-alive",
    }

try:
    data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
    link = data.json()["destination"]
    system("cls")
    print(banner)
    print(purple(f" ==> Ergebnis : {link}"))
except:
    system("cls")
    print(banner)
    print(red(" [!] Fehler"))

system("pause >nul")
