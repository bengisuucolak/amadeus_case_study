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
    my_second_element.send_keys("los angeles")
    find_my_second_element = driver.find_element_by_xpath('//*[@id="headlessui-combobox-option-:r9:"]')   
    find_my_second_element.click()

except:
    print("there is no los angeles option ")

try:

    x_list = driver.find_elements_by_xpath("//ul[@class='grid grid-cols-1 gap-x-6 gap-y-8 lg:grid-cols-3 xl:gap-x-8']/li[@class='overflow-hidden rounded-xl border border-gray-200']")
    x_item =len(x_list)
    print("found ", x_item, " item")
    print("the tast case is pass")
except:
    print("there is no item")

