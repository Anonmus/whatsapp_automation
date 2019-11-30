from selenium import webdriver
import time

# if you don't want to scant qr code again again
# then set the path according to your computer directory
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\gp896\\AppData\\Local\Google\\Chrome\\User Data\Default")
# if you don't know how to set path then comment the above two line
# and uncomment line 14 and comment line 13


# your need to specify the location fo chromedriver directory
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=options)
# driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
reciver = input('Enter the name of reciver/group : ')  # reciver needs to be in your recent chat
message = input('Enter your message : ')
count = int(input('Enter the count : '))
input('Enter anything after scanning QR code')

reciver = driver.find_element_by_xpath('//span[@title = "{}"]'.format(reciver))
reciver.click()
in_box = driver.find_element_by_xpath('//div[@contenteditable="true"]')

for i in range(count):
    in_box.send_keys(message)
    button = driver.find_element_by_class_name('_3M-N-')
    time.sleep(1)  # timer difference between sending messages in second
    button.click()
