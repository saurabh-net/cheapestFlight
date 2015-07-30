import locale
import json
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

files=["dates_BOM.txt"]
#check= raw_input("Enter the flight to analyse!! :")
#fl_no=raw_input("Enter the flight number !!")
prices=[]
scraps=[]
for fi in files:
	fp= open(fi,"r")
	for line in fp:
		flight,flightno,time1,time2,duration,price,scraptime,site,booking=line.strip().split("\t")
		#if(try:try:try:try:flight==check and flightno==fl_no):
		try:
			x= price[4:]
			x=locale.atoi(x)
			print x
			print str(booking)		
			scraps.append([x,str(booking)])
		except ValueError:
			pass


		#prices.append(price[])
wr=open("data_BOM.json","wb")
wr.write(str(scraps))

print 
fp.close()
wr.close()