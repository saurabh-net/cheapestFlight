from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from time import sleep
from bs4 import BeautifulSoup
import datetime


# uncomment if using Firefox web browser
driver = webdriver.Firefox()

urls = ['http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BLR&destinationCountry=IN&flight_depart_date=01/05/2015&ADT=1&CHD=0&INF=0&class=Economy','http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=01/05/2015&ADT=1&CHD=0&INF=0&class=Economy','http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=HYD&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy','http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=MAA&destinationCountry=IN&flight_depart_date=01/05/2015&ADT=1&CHD=0&INF=0&class=Economy','http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=CCU&destinationCountry=IN&flight_depart_date=01/05/2015&ADT=1&CHD=0&INF=0&class=Economy']

"""
http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=01/05/2015&ADT=1&CHD=0&INF=0&class=Economy
http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=HYD&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy
http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=MAA&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy
http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=CCU&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy

"""
#f=open("results.txt","a")
files = ['bangalore.txt','bombay.txt','hyderabd.txt','chennai.txt','kolkata.txt']
i = 0
for url in urls:
    driver.get(url)
    currentFile = files[i]
    f=open(currentFile,"a")
    i= i + 1
    wait = WebDriverWait(driver, 10)
    source = driver.page_source.encode('ascii', 'replace')
    soup = BeautifulSoup(source)
    #print soup.get_text()
    commentHolder = soup.find_all("div", {"class":"singleResultSet"})
    scrapedAt = datetime.datetime.now()
    #print commentHolder
    for item in commentHolder:
        #http://domestic-air-tickets.expedia.co.in/flights/results?from=DEL&to=BOM&depart_date=07/05/2015&adults=1&childs=0&infants=0&dep_time=0&class=Economy&airline=&carrier=&x=57&y=16&flexi_search=nosoup = BeautifulSoup(item)
        airline = item.find("span",{"class":"airline-name"}).get_text()
        airlineClass = item.find("span",{"class":"airline-code"}).get_text()
        departTime = item.find("span",{"class":"depart-city"}).get_text()
        arriveTime = item.find("span",{"class":"time-arrv"}).get_text()
        destination = item.find("span",{"class":"term-arrv"}).get_text()
        duration = item.find("span",{"class":"flight-tim"}).get_text()
        price = item.find("span",{"class":"res-price-dom"}).get_text()
        price = str(price)
        price = price[:-7]
        #stuff_to_write = airline,airlineClass,departTime,arriveTime,duration,price,scrapedAt,"Yatra"
        f.write(str(airline)+'\t'+str(airlineClass)+'\t'+ str(departTime) +'\t' +str(arriveTime) +'\t' +str(duration) +'\t' +str(price) +'\t' +str(scrapedAt)  +'\t'+ 'Yatra.com' + '\n' )
    #print '\n'
    f.close()

driver.quit()

