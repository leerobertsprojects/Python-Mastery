from selenium import webdriver
from time import sleep

safari_browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')

safari_browser.maximize_window()
safari_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

button = safari_browser.find_element_by_class_name('btn-default')
popup = safari_browser.find_element_by_link_text('No, thanks!')

sleep(5)
popup.click()
user_message = safari_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Lee Roberts')
button.click()
sleep(10)
safari_browser.quit()


