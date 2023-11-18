from threading import Thread
from Api import sms, call
from time import sleep
from inspect import getmembers, isfunction 
from os import system, name

SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(0.01)

def bombing(phone, count):
    x = 0
    phone = f"+98{phone[1:]}"
    for j in range(count):
        for k in range(len(SMS_SERVICES)):
            Thread(target=getattr(sms, SMS_SERVICES[k]), args=[phone]).start()
        if (j !=0) and (j % 5) == 0:
            Thread(target=getattr(call, CALL_SERVICES[x]), args=[phone]).start()
            x += 1
            if x > len(CALL_SERVICES) - 1:
            	x = 0
        print(f"\033[1m\033[96mRound \033[1;31m{j+1} \033[1m\033[96mCompleted")
        sleep(0.2)
    printLow("\033[32;1m[\033[1;33mFinished\033[32;1m]")
    
if __name__ == "__main__":
    printLow(f"""\033[32;1m[+] \033[1;33mSMS Api's: \033[32;1m{len(SMS_SERVICES)}\n\033[32;1m[+] \033[1;33mCALL Api's: \033[32;1m{len(CALL_SERVICES)}\n\033[32;1m[+] \033[1;33mDeveloper: \033[32;1m@ExpireSourc""")
    num = input('\n\n\033[32;1m[$] \033[1m\033[96mEnter Phone Number\n\033[1;33m  Ex:09190000000\n \033[1;31m-> \033[32;1m')
    yy = int(input("\n\033[32;1m[$] \033[1;33mEnter The Count of Round of Bombing\n\033[1;31m-> \033[32;1m"))
    system('clear' if name == 'posix' else 'cls')
    printLow("\033[32;1m[+]\033[1;33m Phone Number:\033[1m\033[96m {}\n\033[32;1m[+]\033[1;33m Rounds:\033[1m\033[96m {}\n\n".format(num,yy))
    printLow("\033[32;1m[\033[1;31mStart\033[32;1m]\n")
    bombing(phone=num,count=yy)