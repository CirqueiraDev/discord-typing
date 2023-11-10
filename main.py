# Discord Typing Script

# Author: Cirqueira
# Discord: cirqueira
# Github: https://github.com/CirqueiraDev/

import requests, time

global R,B,C,G,Y,Q
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; G='\033[1;32m'; Y='\033[1;33m'; Q='\033[1;36m'

channelID = "1071872797351096391main.py"   # Put the channel ID here
userToken = "NzU1NTY0NzY4NDM3MzM4MTYy.GNGRuM._YEtusd2m29uuugbqnHAMG8csNPxSWZhttRQH4"   # Place your token here. And don't forget DON'T SHARE IT WITH ANYONE ELSE

def sendTyping():
    headers = {
        "Authorization": userToken,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9023 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
        "X-Discord-Timezone": "America/Sao_Paulo",
        "X-Discord-Locale": "pt-BR",
        "Accept": "*/*",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/@me/" + channelID,
        "Content-Length": "0"
    }
    
    response = requests.post(f"https://discord.com/api/v9/channels/{channelID}/typing", headers=headers) # Request
    
    # Verifying the api response
    if response.status_code == 204:
        print('[%s%s%s] Successful request!'%(G,response.status_code,C))
    elif response.status_code == 401:
        print('[%s%s%s] Request Failed! Verify that your token is correct'%(R,response.status_code,C))
    else:
        print('[%s%s%s] Ops! It looks like you forgot to fill in the variables...'%(R,response.status_code,C))
        print('Please contact me if you need help. %sDiscord%s: %scirqueira%s'%(B,C,Q,C))
        exit()

if __name__ == '__main__':
    print('\n%sPress %sCTRL%s + %sC%s to stop the script!\n'%(C,Y,C,Y,C))
    while True:
        try:
            sendTyping()
            time.sleep(8) # Waiting 8 seconds for the next request
        except KeyboardInterrupt:
            print('\nScript Stopped. Goodbye :D\n')
            exit()