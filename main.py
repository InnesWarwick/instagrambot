
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string
#comment list
comments = ["Classic 48224fb","love it 48224fb","this is my favourtie 48224fb post ever!"]

def main():
    browser = webdriver.Firefox(executable_path="/usr/bin/firefox")
    browser.get('https://www.instagram.com/')
    sleep(5)
    browser.close()





if __name__ == "__main__":
    main()