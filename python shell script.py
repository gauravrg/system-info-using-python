#!/usr/bin/env python
# coding: utf-8

# In[26]:


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



# In[25]:





# In[2]:


# import psutil
# print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
# #Available RAM
# print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
# #Used RAM
# print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
# #RAM usage
# print(f"RAM usage: {psutil.virtual_memory().percent}%")


# In[ ]:


# import speedtest


# In[ ]:


# def perform_speed_test():
#    st = pyspeedtest.SpeedTest()
#    download_speed = st.download() / 1000000  # Convert to Mbps
#    upload_speed = st.upload() / 1000000  # Convert to Mbps

#    return download_speed, upload_speed


# In[ ]:


# download_speed, upload_speed = perform_speed_test()
# print("Download Speed: {:.2f} Mbps".format(download_speed))
# print("Upload Speed: {:.2f} Mbps".format(upload_speed))


# In[ ]:


# import speedtest

# def perform_speed_test():
#    st = speedtest.Speedtest()
#    servers = st.get_best_server()

#    print("Testing download speed...")
#    download_speed = st.download() / 1000000  # Convert to Mbps
#    print("Testing upload speed...")
#    upload_speed = st.upload() / 1000000  # Convert to Mbps

#    return download_speed, upload_speed

# if __name__ == "__main__":
#    download_speed, upload_speed = perform_speed_test()
#    print("Download Speed: {:.2f} Mbps".format(download_speed))
#    print("Upload Speed: {:.2f} Mbps".format(upload_speed))


# In[ ]:



# import speedtest

# st = speedtest.Speedtest()

# print("Download Speed:", st.download())
# print("Upload Speed:", st.upload())
# print("Ping:", st.results.ping)


# In[ ]:


# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# def test_speed():
#     driver = webdriver.Firefox()  # or webdriver.Chrome()
#     driver.get('https://fast.com')
#     time.sleep(60)  # Wait for test to complete
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     speed = soup.find('div', {'class': 'speed-results-container'}).text
#     driver.quit()
#     return speed

# print("Internet speed: ", test_speed())


# In[ ]:


# #screen_size


# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))


# In[ ]:





# In[ ]:





# In[ ]:


# #Current frequency
# print(f"Current CPU frequency: {psutil.cpu_freq().current}")
# #Min frequency
# print(f"Min CPU frequency: {psutil.cpu_freq().min}")
# #Max frequency
# print(f"Max CPU frequency: {psutil.cpu_freq().max}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




