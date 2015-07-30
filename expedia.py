from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import sleep
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from time import sleep as wait
import re
import requests
from collections import namedtuple
import pickle
import os, time
import datetime



###########################################################################################################


expediaResults={}



###########################################################################################################

# uncomment if using Firefox web browser


# uncomment if using Phantomjs
#driver = webdriver.PhantomJS()


class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

	
	
def expediaSearch(start,end,date,adult,child,infant,type):
	dat1=date.split('/')
	dates=""
	for i in dat1:
		dates+=i
	f=open("results.txt","w")
	nowTime=datetime.datetime.now()
	flag=0
	fname=start+'-'+end+'-'+dates+'-'+adult+'-'+child+'-'+infant+'-'+type+'.html'
	if(not(os.path.isfile(fname))):
		flag=1
	if(flag==0):
		createTime=datetime.datetime.fromtimestamp(os.path.getmtime("results.txt"))
		diff=nowTime-createTime
		hours=diff.seconds/3600
		if(hours>2):
			flag=1
	if(flag==1):
		print "Querying server...."
		driver = webdriver.Firefox()
		url = 'http://domestic-air-tickets.expedia.co.in/flights/results?from=DEL&to=BOM&depart_date=13/05/2015&adults=1&childs=0&infants=0&dep_time=0&class=Economy&airline=&carrier=&x=57&y=16&flexi_search=no'
		driver.get(url)

		# set initial page count

	
		
		# sleep here to allow time for page load
		sleep(5)
		source = driver.page_source.encode('ascii', 'replace')
		x=open(fname,"w")
		x.write(source)
		driver.close()
	else:
		print "Recent Record exists..."
		src=open(fname,"r")
		source=src.read()
	
	soup = BeautifulSoup(source)
	#print soup
	results = soup.find_all("tr", {"class":"onward"})
	j=0
	while(j<10):
		soup = BeautifulSoup(str(results[j]))
		airline = soup.find('span', attrs = {'class' : 'weak airline_name'})
		airline=strip_tags(str(airline))
		dep = soup.find('td', attrs = {'class' : 'depart-at'})
		dep=strip_tags(str(dep))
		arr = soup.find('td', attrs = {'class' : 'arrive-at'})
		arr=strip_tags(str(arr))
		dur = soup.find('td', attrs = {'class' : 'total-dur'})
		dur=strip_tags(str(dur))
		price = soup.find('td', attrs = {'class' : 'price'})
		price = price.find('strong')
		price=strip_tags(str(price))
		f.write(airline+'\t'+dep+'\t'+arr+'\t'+dur+'\t'+price+'\n')
		expediaResults[j]=[airline,dep,arr,dur,price]
		j+=1
		print "Adding record no. ",j," ...."

###########################################################################################################			

start=raw_input("Enter Departure Airport: ")
end=raw_input("Enter Arrival Airport: ")
date=raw_input("Enter date (as dd/mm//yyyy): ")
adult=raw_input("Enter number of adults: ")
children=raw_input("Enter number of children: ")
infant=raw_input("Enter number of infants: ")
type=raw_input("Enter class (Economy/Business): ")
expediaSearch(start,end,date,adult,children,infant,type)
