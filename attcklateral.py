from selenium import webdriver
a=input("Technique Id: ")
browser=webdriver.Chrome()
glist=[]
browser.get("https://attack.mitre.org/versions/v6/techniques/"+a+"/")
i=1
while True:
    try:
        s=browser.find_element_by_xpath('''//*[@id="v-attckmatrix"]/div[2]/div/div/div/table[1]/tbody/tr['''+str(i)+''']/td[1]/a''').text
        i=i+1
        glist.append(s)
    except:
        break
print(", ".join(glist))
