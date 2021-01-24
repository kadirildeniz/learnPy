import os
import time

print("enter ip address : ")
ipAdress = '192.168.1.1'
dump = ipAdress
dump = dump.splitlines()
for ip in dump:
    os.system('cls')
    print (' Ping Request', ip)
    print ('-' * 60)
os.system('Ping {0}'.format(ip))
print ('-' * 60)
time.sleep(5)
