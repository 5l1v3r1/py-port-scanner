import sys
import socket
from datetime import datetime

#python port-scnner.py <IP>

if len(sys.argv) == 3:
    target = socket.gethostbyname(sys.argv[1]) #Translet hostname to IPv4
    getport = sys.argv[2].split('-')
else:
    print("Invalid argument")
    print("Usage: python port-scanner.py <IP-Address> <Port range>")
    print("Example:\n python port-scanner.py 192.168.1.1 1-65535")

# Just a banner :P
print('='*55)
print("Scan stared against {}".format(target) + " at " + str(datetime.now()))
print('='*55)

try:
    for port in range(int(getport[0]),int(getport[1])):
        #Maknig variable of the socket object with AF_INT is IPv4 and SOCK_STREAM is Port
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        #setting timeout to 2 second for connection 
        socket.setdefaulttimeout(2)
        #IF result is 0 that means port is open if It's 1 that mean port is closed 
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
            s.close()
        
# If keyboard interruption found
except KeyboardInterrupt:
    print("\n Exiting the program!, Keyboard Interruption found ctr^c")
    sys.exit()

# If host couldn't resolved 
except socket.gaierror:
    print("\n Host could not be resloved")
    sys.exit()

# If couldn't connect to server
except socket.error:
    print("\n Could not connect to server")
    sys.exit()
