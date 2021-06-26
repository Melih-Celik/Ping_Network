import subprocess,socket
import time
from getmac import get_mac_address

figlet="""
 ______ _           _   _   _      _                      _    
|  ____(_)         | | | \ | |    | |                    | |   
| |__   _ _ __   __| | |  \| | ___| |___      _____  _ __| | __
|  __| | | '_ \ / _` | | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |    | | | | | (_| | | |\  |  __/ |_ \ V  V / (_) | |  |   < 
|_|    |_|_| |_|\__,_| |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\\
                   ______                                      
                  |______|
"""

def skip_20():
    for i in range(20):
        print("\n")

print(figlet)
network_range=input("Araligi giriniz (192.168.1.1-100) : ")
skip_20()
base_ip=".".join(network_range.split(".")[:-1])+"."

range_ip=network_range.split(".")[-1].split("-")
beautifier="_________________________________________________________________________________________"
while True:
    print(figlet,"\n\nRange to scan : ",network_range)
    selection=input("1.Scan Live Devices\n0.Exit Program\nYour Choice : ")
    if selection=="1":
        skip_20()
        print("Ip Address\t | Mac Address\t\t | Status\t | Hostname")
        print(beautifier)

        for i in range(int(range_ip[0]),int(range_ip[1])+1):
            try:
                if "unreachable" in str(subprocess.check_output("ping "+base_ip+str(i)+" -n 1 -l 1",timeout=1)):
                    pass
                else:
                    try:
                        hostname=socket.gethostbyaddr(base_ip+str(i))[0]
                    except:
                        hostname="Unnamed Host"
                    print(base_ip+str(i)+"\t | "+get_mac_address(ip=base_ip+str(i))+"\t"+" | Responding \t | "+hostname+"\n"+beautifier)
            except:
                pass
            print("%","{:.1f}".format(((int(i)-int(range_ip[0]))*100)/(int(range_ip[1])+1-int(range_ip[0]))),end="\r")
            if i==int(range_ip[1]):
                input("Scan is completed.\nPress any button to go to menu...")
                skip_20()
    elif selection=="0":
        print("Terminating the program...")
        time.sleep(3)
        break
    else:
        skip_20()
        continue