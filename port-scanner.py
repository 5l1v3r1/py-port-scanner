import sys
import socket
from datetime import datetime
import threading

#python port-scnner.py <IP>
threads=[]
time1 = datetime.now()
if len(sys.argv) == 3:
    host = socket.gethostbyname(sys.argv[1]) #Translet hostname to IPv4
    getport = sys.argv[2].split('-')
else:
    print("Invalid argument")
    print("Usage: python port-scanner.py <IP-Address> <Port range>")
    print("Example:\n python port-scanner.py 192.168.1.1 1-65535")

# Just a banner :P
print('='*65)
print("Scan started against {}".format(host) + " at " + str(datetime.now()))
print('='*65)


def scan(host,ports):
        socket.setdefaulttimeout(1)
        result=socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect_ex((host,ports))
        if result == 0:
            print("Discovered open port {}/tcp".format(ports))

            socket.socket(socket.AF_INET,socket.SOCK_STREAM).close()

for ports in range(int(getport[0]),int(getport[1])):
    t1 = threading.Thread(target=scan,args=(host,ports))
    threads.append(t1)
    t1.start()

for thread in threads:
    thread.join()


time2 = datetime.now() #Getting time after loop is completed
total = time2 - time1  #Total time taken 
#Just another banner
print ("="*45)
print ("Scanning completed in: ",total)
print ("="*45)
