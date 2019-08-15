
# WARNING! All changes made in this file will be lost!
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from tkinter import *
from tkinter import ttk


def spamfriend(receivers, message):
    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    receivers_names = str(receivers.get('1.0', 'end')).split('\n')
    msg = str(message.get('1.0', 'end'))
    print(receivers_names)
    print(msg)
    for i in receivers_names:
        person = '"'+i+'"'
        startspammingfriend(person, msg, wait)


def startspammingfriend(person, msg, wait):

    target = person

    # Replace the below string with your own message
    string = msg

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    input_box.send_keys(string + Keys.ENTER)


if __name__ == "__main__":
    root = Tk()
    Label(root, text='Enter one name per line').grid(row=1, column=0)
    receivers = Text(root)
    receivers.grid(row=1, column=1)
    Label(root, text='Enter message').grid(row=2, column=0)
    message = Text(root)
    message.grid(row=2, column=1)

    button = ttk.Button(root, text='Send', command=lambda: spamfriend(receivers, message))
    button.grid(row=3, column=1)
    root.mainloop()
