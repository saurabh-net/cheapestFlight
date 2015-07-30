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
import sched
import time


###########################################################################################################

scheduler = sched.scheduler(time.time, time.sleep)


###########################################################################################################


def crawler():
	airports=['del','bom','hyd','blr','maa','ccu']
	print "Querying server...."
	driver = webdriver.Firefox()
	for start in airports:
		for end in airports:
			if(start!=end):
				print "Saving file for ",start," to ",end," ..."
				fname=start+'-'+end+'-01052015-1-0-0-economy.html'
				url = 'http://domestic-air-tickets.expedia.co.in/flights/results?from='+start+'&to='+end+'&depart_date=01/05/2015&adults=1&childs=0&infants=0&dep_time=0&class=economy&airline=&carrier=&x=57&y=16&flexi_search=no'
				driver.get(url)
				sleep(5)
				source = driver.page_source.encode('ascii', 'replace')
				x=open(fname,"w")
				x.write(source)
	driver.close()

	
###########################################################################################################	
	
time=0
while (1):
	crawler()
	time.sleep(3*3600)
	
#crawler()