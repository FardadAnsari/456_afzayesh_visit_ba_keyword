from selenium.webdriver.chrome.options import Options
from selenium import webdriver as Wee
import random
from time import sleep
from selenium.webdriver.common.keys import Keys
import wget
import os
import zipfile


proxy_list=[]
for ip in open(r"C:\Users\Pyt\Desktop\proxy.txt"):
        proxy_list.append(ip)


def Weemarket_openbrowser(PROXY):
        option = Options()
        option.add_argument('--disable-infobars')
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_argument('lang=en')
        option.add_argument("--proxy-server=%s" % PROXY)
        #option.add_argument('--headless')

    
        option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
        })
        
        chromedriver_path ="C:\chromedriver.exe"
        browser = Wee.Chrome(options=option, executable_path=chromedriver_path)



        return browser

count=0
elf=True
for ips in proxy_list:
        
        try:
            s_1=random.randint(2,6)
            sleep(s_1)
            count=count+1
            interact=Weemarket_openbrowser(ips)
            interact.get("https:\\www.google.com")
            sleep(s_1)
            search_box = interact.find_element_by_name('q')
            search_box.send_keys("Dragon Palace takeaway")
            sleep(s_1)
            search_box.send_keys(Keys.RETURN)
            sleep(s_1)
            
            page_num=0
            
            while elf=True:
                
                list_753=[]
                Result_website=interact.find_elements_by_class_name('iUh30.tjvcx')
                for webs in Result_website:
                    if webs.text=="dragonpalace-takeaway.co.uk":
                        list_753.append(webs)
                    else:
                        pass
                page_num=page_num+1
                
                if len(list_753) != 0:
                    list_753[0].click()
                    sleep(4)
                    #All operations related to the intended web address 
                    interact.close()
                    elf=False
                else:
                    page_num=interact.find_elements_by_class_name('SJajHc NVbCr')
                    page_num[page_num].click()
                    sleep(4)
                    
                        
                     
                        

            print("I found the website")
            sleep(60)
            interact.close()
            print(" Interaction number "+ str(count) +" was successful !")

        except:
            print(" Interaction number "+ str(count) +" was Unsuccessful !")