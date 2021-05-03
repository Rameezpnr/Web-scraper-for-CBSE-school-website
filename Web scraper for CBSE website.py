# work by Mohammed Ramees
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx")
print(driver.title)

pages = input("how many pages of data do you want to collect? ")
pages = int(pages)
details = input("do you only need name of the school? (y/n)")

search = driver.find_element_by_id("optlist_0")
search.click()
search = driver.find_element_by_id("keytext")
search.send_keys('a')
search.send_keys(Keys.RETURN)

#try:
#    main = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.__class__, "repItem"))
#    )
#    articles = main.find_elements_by_class("repItem")
#    for articles in repitem:
#        header = article.find_element_by_class_name("repItem")
#        print(header.text)

#except:
#    driver.quit()

if details == "y" :
    print("name of schools:")
    for num in range(pages):
        #num = (0,1,2,3,4,5,6,7,8,9,10,11,12)
        for numbers in range (0,13):
            results = driver.find_elements_by_id("hyp")
            print("{}".format(results[numbers].text))


        #num = (0,1,2,3,4,5,6,7,8,9,10,11)
        for numbers in range (0,12):
            results = driver.find_elements_by_id("Hyperlink1")
            print("{}".format(results[numbers].text))


        button = driver.find_element(By.ID, 'Button1')
        button.send_keys(Keys.RETURN)


else:
    print("All details of school is given below")
    for num in range(pages):
        address = driver.find_element_by_id('T1')
        newa = address.text[50:]
        print(newa)
        #address = driver.find_elements_by_css_selector('tbody')
        #print(address[num].text)
        button = driver.find_element(By.ID, 'Button1')
        button.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()


#these are the tried methods which are not currently using.

#school=find_elements_by_xpath('//span[@id="hyp"][1]')
#for value in school:
 #   print(value.text)



#othername = driver.find_elements_by_id("hyperlink1")
#print(othername)



#name = driver.find_element_by_id("hyp")




