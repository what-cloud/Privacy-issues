from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from urllib.request import urlretrieve

#You should be using Robot to send all of your key presses to the system level Alert. Including your user and PW.
#A security dialogue is not a JavaScript level dialogue box

def searchpage():
	global namelist
	search = driver.find_elements_by_class_name("profile-link")
	for result in search:
		namelist.append(result.text)

	search3 = driver.find_elements_by_xpath("//*[@id='bodyarea']/table/tbody/tr/td/table") #get photos
	search4 = driver.find_elements_by_xpath("//*[@id='bodyarea']/table/tbody/tr/td/*/tbody/tr/td/table/tbody/tr[1]/td[3]")  #moves from Img embedded in<a> (1 level) embedded in <span> (2 levels), and search for next h4 #get names of these photos
	count=0
	for result in search4:
		count=count+1
		photolist.append(search4[count-1].text)
		

driver = webdriver.Firefox()


#https://bitcointalk.org/index.php?action=profile;u=3;sa=showPosts;start=520





print (driver.page_source)
#driver.navigate().refresh();


sleep(1)

actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE)
actions.perform()
#print (driver.page_source)
namelist=[]
photolist=[]


pages=20
driver.get('https://bitcointalk.org/index.php?action=profile;u=3;sa=showPosts;start='+str(pages))


while driver.find_elements_by_xpath("//*[@id='bodyarea']/table/tbody/tr/td/*/tbody/tr/td/table/tbody/tr[1]/td[3]") and pages<521:
	searchpage()
	print("search pages:",pages)
	sleep(3)
	pages = pages + 20
	driver.get('https://bitcointalk.org/index.php?action=profile;u=3;sa=showPosts;start='+str(pages))
	
	#https://bitcointalk.org/index.php?action=profile;u=3;sa=showPosts;start=0
	#https://bitcointalk.org/index.php?action=profile;threads;u=3;sa=showPosts;start=
	

#//div[contains(@class, "myClass")]/img/@src

#https://homeport.rccl.com/people-finder/?query=85000731&pg=2



print (namelist)
print (photolist)