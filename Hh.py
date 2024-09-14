#https://t.me/uiujq
import os
import requests
import random
from colorama import *
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
c = Fore.CYAN
(c + requests.get('http://artii.herokuapp.com/make?text= o m a  r').text)



rt = requests.session()
R = '1234567890'
M ='qwertyuiopasdfghjklzxcvbnm'
A = '.'
D = '_'
litters = R + M
u = ''
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
print(B+'━'*67)
print('\x1b[1;38;5;125m')
id = input('    𝑰𝑫 ➱ ')

print('\x1b[1;38;5;213m')

token = input('    T𝑶𝑲𝑬𝑵 ➯ ')
print(f'{Y}  ملاحضه الاداة تصيد مبند افحص اليوزر  ')
hea = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',

    }
while True:
	user = str("".join(random.choice(litters)for x in range(2)))
	user1 = str("".join(random.choice(litters)for x in range(1)))
	usernames = user + '.' + user1
	tiko = f'https://www.tiktok.com/@{usernames}?'
	reqsnd = rt.get(tiko, headers=hea).status_code
	if reqsnd == 404:
	        os.system('clear')
	        print(g + f'\033[1;32m ⋘─────━صوفي━─────⋙		   																				✅ 𝚄𝚂𝙴𝚁 ➠@{usernames}\n⋘─────━صوفي━─────⋙		  																			𝙋𝙮 ➪ @M02MM : @uiujq')
	        
	        bot = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= ⋘─────━صوفي━─────⋙		   																				✅ 𝚄𝚂𝙴𝚁 ➠@{usernames}\n⋘─────━صوفي━─────⋙		  																			𝙋𝙮 ➪ @M02MM : @uiujq')"
	        rt.get(bot)
	        
	else:
		 os.system('clear')
		 print(r + f'\x1b[1;91m   ﮩ٨ـﮩﮩ٨ـﮩـﮩﮩ٨ـ🫀ﮩ٨ـﮩﮩ٨ـﮩﮩ٨ـ:   \x1b[1;38;5;209m   {usernames}\x1b[1;38;5;227mغير متاح ')
