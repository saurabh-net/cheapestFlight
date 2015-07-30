from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

# uncomment if using Firefox web browser

dict_1 = {}

#url = 'http://www.goibibo.com/#flight-searchresult/#air-DEL-BOM-20150425--1-0-0-E'


station1 = raw_input(" Select Boarding Station code\n").upper()
station2 = raw_input("Select Destination code\n").upper()

depart = raw_input("Select departure date in yyyymmdd format:	")
retur = ""
if(raw_input("Return trip (select y or n) ")== 'y'):
	retur = raw_input("Select return date in yyyymmdd format:	")

adults = raw_input("Enter number of adult passengers ")
children = raw_input("Enter number of children (2-12 years) ")
infants = raw_input("Enter number of infants ")

Class = raw_input("Select Class (E, B, F or W)").upper()


url = 'http://www.goibibo.com/#flight-searchresult/#air-' + station1 + '-' + station2 + '-' + depart
if not retur:
	url = url + '--' + adults + '-' + children + '-' + infants + '-' + Class
else:
	url = url + '-' + retur + '-' + adults + '-' + children + '-' + infants + '-' + Class

#print(url)
driver = webdriver.Firefox()
#WebDriver driver = new ChromeDriver()
driver.get(url)

#wait = WebDriverWait(driver, 10)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ft_results")))
sleep(5)

source = driver.page_source.encode('ascii', 'replace')
soup = BeautifulSoup(source)
#print soup
commentHolder = soup.find_all("div", {"class":"ft_results"})
i = 0
#print commentHolder
for item in commentHolder:
	soup = BeautifulSoup(str(item))
	time = soup.find("big")
	time1 = time.get_text().split()
	time2 = time1[0]
	#print time2
	span = soup.find("ins", {"class":"ft_res_v"})
	span0 = BeautifulSoup(str(span))
	span1 = span0.find("span")
	span2 = span1.get_text()
	#print span2
	name = soup.find("samp")
	name0 = BeautifulSoup(str(name))
	name1 = name0.find("span")
	name3 = BeautifulSoup(str(name1)).find("i").get_text()
	name2 = name1.get_text().split()[0] + " " + name3
	#name2 = name1.get_text().split()[0] + " " + name1.get_text().split()[1]
	#print name2
	price = soup.find("em")
	price0 = BeautifulSoup(str(price)).find("a", {"class":"ft_overlay", "name":"normalfare"}).get_text()
	price1 = price0.split()[0][2:]

	attr_list = [time2, span2, price1]
	dict_1[name2] = attr_list
	i = i + 1
	if i>9:
		break

print dict_1