import requests,os,sys
from time import sleep
from datetime import datetime
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#NORI-TOOL
info = f'{red}[{trang}+{red}]'
hd = f'{red}[{trang}•_•{red}] {trang}=> {green}'
#BANNER
os.system("cls" if os.name == "nt" else "clear")
banner = f'''{xduong}███╗  ██╗ █████╗ ██████╗ ██╗      ████████╗ █████╗  █████╗ ██╗
{xduong}████╗ ██║██╔══██╗██╔══██╗██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
{xduong}██╔██╗██║██║  ██║██████╔╝██║█████╗   ██║   ██║  ██║██║  ██║██║
{xduong}██║╚████║██║  ██║██╔══██╗██║╚════╝   ██║   ██║  ██║██║  ██║██║
{xduong}██║ ╚███║╚█████╔╝██║  ██║██║         ██║   ╚█████╔╝╚█████╔╝███████╗
{xduong}╚═╝  ╚══╝ ╚════╝ ╚═╝  ╚═╝╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚══════╝
{red}────────────────────────────────────────────────────────────────────────
{info}{tim} Admin: Quang Đức
{info}{yellow} Zalo: 0364218196
{info}{xnhac} Box Zalo:
{info}{blue} Youtube:
{red}────────────────────────────────────────────────────────────────────────\n'''
for X in banner:
 sys.stdout.write(X)
 sys.stdout.flush()
 sleep(0.00125)