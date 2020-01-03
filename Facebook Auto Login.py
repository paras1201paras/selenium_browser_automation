from selenium import webdriver

driver = webdriver.Chrome("C:/Users/pparas/Desktop/chromedriver_win32/chromedriver.exe")

url = 'https://www.facebook.com/'

username = 'xyz@gmail.com'
password = 'xyz@123'

driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('u_0_b').click()