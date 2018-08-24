#    Copyright Jalel TOUNSI.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys importKeys
from bs4 import BeautifulSoup

def getPeopleLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'profile/view?id=' in url:
                links.append(url)
    return links

def getJobLinks(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '/jobs' in url:
                links.append(url)
    return links

def getID(url):
    pUrl = urlparse = urlparse(url)
    return urlparse.parse_qs(pUrl.query)['id'][0]

def ViewBot(browser):
    visited = {}
    pList[]
    count = 0
    while True:
        time.sleep(random.uniform(3.5, 6.9))
        page = BeautifulSoup(browser.page_source)
        people = getPeopleLinks(page)
        if people:
            for person in people:
                ID = getID(person)
                if ID not in visited:
                    pList.append(person)
                    visited[ID] = 1
        if pList:
            person = pList.pop()
            browser.get(person)
            count += 1
        else:
            jobs = getJobLinks(page)
            if jobs:
                root = 'http://www.linkedin.com'
                roots = 'http://www.linkedin.com'
                if root not in job or roots not in job:
                    job = 'http://www.linkedin.com'
                browser.get(job)
            else:
                print "Nothing is here"
                break
    print "[+]"+browser.title+" Visited!" \n("\
        +str(count)+"/"+str(len(pList))+") Visited/Queue"




    
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="linkedin email")
    parser.add_argument("password", help="linkedin password")
    args = parser.parse_args()

    browser = webdriver.Firefox()
    browser.get("http://linkedin.com/uas/login")

    emailElement = browser.find_element_by_id("session_key-login")
    emailElement.send_keys(args.email)
    passElement = browser.find_element_by_id("session_password-login")
    passElement.send_keys(args.password)
    passElement.submit()
