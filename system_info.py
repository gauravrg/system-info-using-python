# importing the module 
import subprocess
import psutil
import platform
from requests import get

# traverse the software list 
Data = subprocess.check_output(['wmic', 'product', 'get', 'name']) 
a = str(Data) 

# try block 
try: 

# arrange the string 
    for i in range(len(a)): 
        print(a.split("\\r\\r\\n")[6:][i]) 

except IndexError as e: 
     print("All install Software List is Done")
        


#Computer network name
print(f"Computer network name: {platform.node()}")
#Machine type
print(f"Machine type: {platform.machine()}")
#Processor type
print(f"Processor type: {platform.processor()}")
#Platform type
print(f"Platform type: {platform.platform()}")
#Operating system
print(f"Operating system: {platform.system()}")
#Operating system release
print(f"Operating system release: {platform.release()}")
#Operating system version
print(f"Operating system version: {platform.version()}")
      
        
        
#Physical cores
#No of core and threads of CPU
print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
#Logical cores
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")


#RAM Size ( In GB )


print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
#Available RAM
print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
#Used RAM
print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
#RAM usage
print(f"RAM usage: {psutil.virtual_memory().percent}%")



#print ip address
from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))

#print mac address
import uuid

a = hex(uuid.getnode())
print("max address is:" ,a)