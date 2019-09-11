from bs4 import BeautifulSoup
from selenium import webdriver
import urllib3
import numpy as np
from selenium.webdriver.common.keys import Keys
import easygui
import random

def scrape(url):
    http = urllib3.PoolManager()
    response = http.request('GET',url)
    soup = BeautifulSoup(response.data,features="html.parser")
    newLinks = []
 

    for link in soup.find_all('a', href=True):
        if link['href'] != '#':
            if link['href'][:5] == 'https':
                newLinks.append(link['href'])
    return newLinks

def findUniqueLinks(path,newLinks):
    pastLinks = []
    with open('D:/OnionProject/savedlinks.txt','r+') as myfile:
        #generate past links
        for line in myfile:
            pastLinks.append(line[:-1])
        unseenList = np.setdiff1d(newLinks,pastLinks)
        return unseenList

def openLink(link,driver,number):
    driver.get(str(link))
    mystring = str(number) + " new articles remaining"
    easygui.msgbox(mystring, 'next')
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    with open('D:/OnionProject/savedlinks.txt','a') as myfile:
        myfile.write(link + '\n')

def openList(mylist):
    driver = webdriver.Chrome('D:/OnionProject/chromedriver')   
    driver.get('https://www.google.com')
    driver.maximize_window()
    for counter, element in enumerate(mylist):
        number = len(mylist) - counter - 1
        openLink(element,driver,number)