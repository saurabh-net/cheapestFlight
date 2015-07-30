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
format = '%d/%m/%Y'
some_day = datetime.date.today()
seven_day = datetime.timedelta(days=7)
#tomorrow = today + _day





# """
# http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=01/08/2015&ADT=1&CHD=0&INF=0&class=Economy
# http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=HYD&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy
# http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=MAA&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy
# http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=CCU&destinationCountry=IN&flight_depart_date=03/07/2015&ADT=1&CHD=0&INF=0&class=Economy

# """

#f=open("results.txt","a")
files = ['bangalore.txt','bombay.txt','hyderabd.txt','chennai.txt','kolkata.txt']
scrapedAt = datetime.datetime.now()
f=open('dates_CCU2.txt',"a")

for x in range(50):
    some_day2 = some_day.strftime(format)
    url = 'http://flight.yatra.com/air-search/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=CCU&destinationCountry=IN&flight_depart_date=' + some_day2 +'&ADT=1&CHD=0&INF=0&class=Economy'
    driver.get(url)
    #currentFile = files[i]
    #i= i + 1
    wait = WebDriverWait(driver, 10)
    sleep(5)
    source = driver.page_source.encode('ascii', 'replace')
    soup = BeautifulSoup(source)
    #print soup.get_text()
    commentHolder = soup.find("div", {"class":"singleResultSet"})
    #print commentHolder

    #http://domestic-air-tickets.expedia.co.in/flights/results?from=DEL&to=BOM&depart_date=07/05/2015&adults=1&childs=0&infants=0&dep_time=0&class=Economy&airline=&carrier=&x=57&y=16&flexi_search=nosoup = BeautifulSoup(commentHolder)
    airline = commentHolder.find("span",{"class":"airline-name"}).get_text()
    airlineClass = commentHolder.find("span",{"class":"airline-code"}).get_text()
    departTime = commentHolder.find("span",{"class":"depart-city"}).get_text()
    arriveTime = commentHolder.find("span",{"class":"time-arrv"}).get_text()
    destination = commentHolder.find("span",{"class":"term-arrv"}).get_text()
    duration = commentHolder.find("span",{"class":"flight-tim"}).get_text()
    price = commentHolder.find("span",{"class":"res-price-dom"}).get_text()
    price = str(price)
    price = price[:-7]
    #stuff_to_write = airline,airlineClass,departTime,arriveTime,duration,price,scrapedAt,"Yatra"
    f.write(str(airline)+'\t'+str(airlineClass)+'\t'+ str(departTime) +'\t' +str(arriveTime) +'\t' +str(duration) +'\t' +str(price) +'\t' +str(scrapedAt)  +'\t'+ 'Yatra.com' + '\t'+ str(some_day2)+ '\n' )
    print x
#print '\n'
    #f.close()
    some_day = some_day + seven_day



driver.quit()

