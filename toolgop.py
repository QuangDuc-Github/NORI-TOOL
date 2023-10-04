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
#Library
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json, os, sys
from datetime import date
from datetime import datetime
from time import sleep,strftime
time = (datetime.now().strftime('%H:%M:%S'))
import socket
from pystyle import *
#====#
ip = requests.get('https://checkip.amazonaws.com').text.strip()
info = f'{red}[{trang}+{red}]'
#Check Key

#NORI-TOOL
#Nori Tool
today = datetime.now().strftime('%d/%m/%Y')
time = (datetime.now().strftime('%H:%M:%S'))
ip = requests.get('https://checkip.amazonaws.com').text.strip()
info = f'{red}[{trang}+{red}]'
hd = f'{red}[{trang}•_•{red}] {trang}=> {green}'
gachngang = f'{red}────────────────────────────────────────────────────────────────────────'

def banner():
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
{info}{luc} Chúc Bạn Dùng Tool Vui Vẻ
{info}{luc} IP Hiện Tại Của Bạn Là:{trang} {ip}
{info}{luc} Hôm Nay Là Ngày:{trang} {today}
{info}{luc} Bạn Vào Tool Lúc:{trang} {time}
{red}────────────────────────────────────────────────────────────────────────'''
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
  sleep(0.00125)
banner()
tool = f"""
 {do}╔═════════════════════╗
 {do}║  {vang}Tool Trao Đổi Sub  {do}║
 {do}╚═════════════════════╝
 {hd}Nhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB
 {hd}Nhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS Pro5
 {hd}Nhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Tiktok
 {red}────────────────────────────────────────────────────────────────────────
 {do}╔══════════════════════╗
 {do}║ {vang}Tool Tương Tác Chéo  {do}║
 {do}╚══════════════════════╝
 {hd}Nhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TTC FB {trang}[Đang Update]
 {hd}Nhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TTC Pro5 {trang}[Đang Update]
 {hd}Nhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC Tiktok {trang}[Đang Update]
 {red}────────────────────────────────────────────────────────────────────────
 {do}╔═════════════════════╗
 {do}║  {vang}  Tool TikTok      {do}║
 {do}╚═════════════════════╝
 {hd}Nhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool Buff View TikTok {trang}[Đang Update]
 {hd}Nhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Buff Tim TikTok {trang}[Đang Update]
 {red}────────────────────────────────────────────────────────────────────────
 {do}╔═════════════════════╗
 {do}║     {vang}Tool Pro5       {do}║
 {do}╚═════════════════════╝
 {hd}Nhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool REG PRO5 + UP AVT
 {hd}Nhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Buff View Story Pro5 
 {hd}Nhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool Buff Reaction Bằng Page Pro5 {trang}[Đang Update]
 {hd}Nhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Share Max Speed Bằng Token Pro5 {trang}[Đang Update]
 {hd}Nhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Buff Follow Bằng Page Pro5
 {hd}Nhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Buff Mem Group Bằng Page Pro5
 {hd}Nhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool Chuyển Quyền Admin Page Pro5
 {hd}Nhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Buff Comment Pro5 {trang}[Đang Update]
 {hd}Nhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Kích Hoạt Pro5 {trang}[Đang Update]
 {red}────────────────────────────────────────────────────────────────────────"""
 #{do}╔══════════════════════════╗
 #{do}║ {vang}Tool Công Cụ + Tiện Ích  {do}║
 #{do}╚══════════════════════════╝

print(tool)
chon = input("\u001b[31;1m[\033[1;37m+\u001b[31;1m] \u001b[32;1mNhập Lựa Chọn :\033[1;33m ")

#TDS
if chon == '1':
 exec(requests.get('https://run.mocky.io/v3/cd6e61a8-5525-493c-8d31-a423b04b3746').text)
if chon == '2':
 exec(requests.get('https://run.mocky.io/v3/4850b017-4679-4fd5-9346-2972f222c051').text)
if chon == '3':
 exec(requests.get('https://run.mocky.io/v3/6839c92f-20c4-42ea-9d18-66b023ebf029').text)
if chon == '4':
 exec(requests.get('').text)
if chon == '5':
 exec(requests.get('').text)
if chon == '6':
 exec(requests.get('').text)
if chon == '7':
 exec(requests.get('').text)
if chon == '8':
 exec(requests.get('').text)
if chon == '9':
 exec(requests.get('https://run.mocky.io/v3/e5b446ee-c153-4f28-8395-d02ab75352d2').text)
if chon == '10':
 exec(requests.get('https://run.mocky.io/v3/cd18aa6a-28f6-444f-bf60-8f45765e4682').text)
if chon == '11':
 exec(requests.get('').text)
if chon == '12':
 exec(requests.get('').text)
if chon == '13':
 exec(requests.get('https://run.mocky.io/v3/e738c2f9-cdbd-492f-9a99-9d85778ea327').text)
if chon == '14':
 exec(requests.get('https://run.mocky.io/v3/8d9febc0-2a56-4a9e-a9e0-6c1bd4020f4c').text)
if chon == '15':
 exec(requests.get('https://run.mocky.io/v3/fce051d3-6bd2-4956-842d-aa15bc18dd8c').text)
if chon == '16':
 exec(requests.get('').text)
if chon == '17':
 exec(requests.get('').text)
