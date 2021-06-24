#!/usr/bin/env python
# coding: utf-8

# In[181]:


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd





driver = webdriver.Chrome('/Users/anubhavanand/Downloads/chromedriver')


driver.get('https://www.linkedin.com')
time.sleep(2)
time.sleep(2)
driver.find_element_by_link_text('Sign in').click()


###################################login#######################################


username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

########################Enter Username and Password############################

username.send_keys('username')
password.send_keys('Password')

time.sleep(4)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()


df = pd.read_csv('/Users/anubhavanand/Desktop/indian_ceo.csv')

x=df['ceo']

for p in x:
    driver.find_element_by_xpath("//input[@type='text']").send_keys(p)
    
    driver.find_element_by_xpath("//input[@type='text']").send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    elems = driver.find_elements_by_xpath("//a[@href]")
    
    link=elems[7].get_attribute("href")

    driver.get(link)
    
    time.sleep(3)
      
    all_button = driver.find_elements_by_tag_name("button")
    
    more_buttons = [btn for btn in all_button if btn.text == "More"]

    more_buttons[0].click()
    
    all_buttons = driver.find_elements_by_tag_name("span")
    
    more_button_connect = [btn for btn in all_buttons if btn.text == "Connect"]
    
    more_button_connect[0].click()
    
    some=driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]/span')
    
    if (some.text =="Connect"):
        
        some.click()
        
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        
        driver.execute_script("arguments[0].click();", send)
    else:
        
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        
        driver.execute_script("arguments[0].click();", send)
        
    time.sleep(2)


# In[ ]:




