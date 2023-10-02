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
#KEY
url = 'https://noritool.000webhostapp.com/key.html?key='+key
web1s = requests.get(f'https://web1s.com/api?token=9aad313d-2857-4610-8c8f-c0cac9b14538&url={url}').json()
if web1s['status']=="error": 
	print(web1s['message'])
	quit()
else:
	link_key=web1s['shortenedUrl']
#Check Key
today = datetime.now().strftime('%d/%m/%Y')
day = int(datetime.now().strftime('%d'))
month = int(datetime.now().strftime('%m'))
year = int(datetime.now().strftime('%y'))
key1 = day+month+year*13*4*2009
key2 = str(key1*1342009)
key = 'Nori'+key2
ip = requests.get('https://checkip.amazonaws.com').text.strip()
time = (datetime.now().strftime('%H:%M:%S'))
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
{red}────────────────────────────────────────────────────────────────────────
{info}{luc} IP Hiện Tại Của Bạn Là:{trang} {ip}
{info}{luc} Hôm Nay Là Ngày :{trang} {today}
{info}{luc} Bạn Vào Tool Lúc:{trang} {time}
{info}{luc} Link Lấy Key:{trang}
{info}{xnhac} Key Được Share Free Trong Box Zalo AE Vào Lấy Nhé 
{red}────────────────────────────────────────────────────────────────────────\n'''
for X in banner:
 sys.stdout.write(X)
 sys.stdout.flush()
 sleep(0.00125)
