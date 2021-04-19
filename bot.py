from bs4 import BeautifulSoup
from selenium import webdriver
import time
TOTAL_UNIVERSITIES = 225

browser = webdriver.Chrome()
universities = list()
i = 0
while i < TOTAL_UNIVERSITIES:
    url = "https://www.hec.gov.pk/english/universities/pages/recognised.aspx#k=#s=%d" % (i)
    browser.get(url)
    time.sleep(15)
    tableBody = browser.find_element_by_tag_name('tbody').get_attribute('innerHTML')
    soup = BeautifulSoup(tableBody, 'lxml')
    for tr in soup.find_all('tr'):
        university = list()
        for index,td in enumerate(tr.find_all('td')):
            # fetch url of university from first data cell
            if(index == 0):
                university.append(td.a.get('href').replace(',','%2C'))
            university.append(td.text.replace(',',' ').strip())
        print(university)
        universities.append(university)
    i = len(universities) + 1


with open('universities.csv','w') as f:
    f.write('url,name,sector,govt,discipline,province,city\n')
    for u in universities:
        for d in u:
            f.write(d + ",")
        f.write('\n')
