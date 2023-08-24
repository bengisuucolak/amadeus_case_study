from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://flights-app.pages.dev/" )
driver.implicitly_wait(8)


try:
    my_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-input-:Rq9lla:"]')    
    my_element.click()
    my_element.send_keys("istanbul")
    find_my_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-option-:r0:"]/div')
    find_my_element.click()
except:
    print("there is no istanbul option ")

try:
    my_second_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-input-:Rqhlla:"]')    
    my_second_element.click()
    my_second_element.send_keys("istanbul")
    find_my_second_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-option-:r7:"]')
    find_my_second_element.click()
    print("because you can enter the same option, there is an error ")
except:
    print("there is no istanbul option ")

try: 
    my_element.click()
    my_element.clear()
    my_second_element.click()
    my_second_element.clear()
except:
    print("because you can't clear the box, there is an error ")

try:  
    my_element.click()
    my_element.send_keys("istanbul")
    find_my_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-option-:re:"]/div')
    find_my_element.click()
    my_second_element.click()
    my_second_element.send_keys("los angeles")
    find_my_second_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-option-:rn:"]/div')
    find_my_second_element.click()
    print("there is 2 flight from İstanbul to Los Angeles")

except:
    print("there is no flight from istanbul to los angeles")

"""
try: 
    my_element.click()
    my_element.clear()
    my_second_element.click()
    my_second_element.clear()
except:
    print("because you can't clear the box, there is an error ")

"""
