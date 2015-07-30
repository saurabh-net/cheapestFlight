import locale
import json
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

files=["dates_CCU_Experia.txt",]
#check= raw_input("Enter the flight to analyse!! :")
#fl_no=raw_input("Enter the flight number !!")
prices=[]
scraps=[]
for fi in files:
	fp= open(fi,"r")
	for line in fp:
		flight,flightno,time1,time2,duration,price,scraptime,site=line.strip().split("\t")
		#if(flight==check and flightno==fl_no):
		try:
			x= price[4:]
			print x
			x=locale.atoi(x)
			print x
			scraps.append(x)
		except ValueError:
			pass


		#prices.append(price[])
wr=open("data_ex.json","wb")
wr.write(str(scraps))

print 
fp.close()
wr.close()