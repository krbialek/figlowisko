	
	
def check():	
	from bs4 import BeautifulSoup
	import requests

	URL = "http://31.186.202.2/RBP11112222S2P0Y0/20191111225918885526/20191111225753467159/20191111225545442922/2019111122584099999/20191111225840411098/20191109105608005499/0/0/"
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	child_soup = soup.find_all('center')



	# Temperatura na tafli lewa, prawa i hala

	taf_l 	= None
	taf_p 	= None
	hal 	= None


	for i in child_soup:
	    #print(i.text.strip().split())
	    
	    if i.text.strip().split()[1] == "tafla" and i.text.strip().split()[3] == "lewa":
	    	taf_l = i.text.strip().split()[6]
	    
	    if i.text.strip().split()[1] == "tafla" and i.text.strip().split()[3] == "prawa":
	    	taf_p = i.text.strip().split()[6]
	    
	    if i.text.strip().split()[1] == "wewnątrz" and i.text.strip().split()[2] == "hali":
	    	hal = i.text.strip().split()[5]
	    	
	    #if i.text.strip().split()[1] == "tafla": 
	    #    print(i.text.strip().split()[6])



	url1_off = 'http://192.168.111.15/stat.php?off=1'
	url1_on = 'http://192.168.111.15/stat.php?on=1'
	url2_off = 'http://192.168.111.15/stat.php?off=2'
	url2_on = 'http://192.168.111.15/stat.php?on=2'

	min
	przek_1 = "on"

	#taf_l = 1
	#taf_p = 1
	#hal = 0

	taf_max = max(float(taf_l), float(taf_p))

	print(taf_l, taf_p, hal, taf_max, float(hal) / -5, float(hal) / -4, float(hal) / -3)
	####### WLACZAMY PRZEKAZNIK 1 #############

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa -1 st. oraz mniejsza od +1 st. oraz temperatura na "tafli" jest większa/równa -0.2 st.

	if float(hal) >= -1 and float(hal) < 1 and float(taf_max) >= -0.2:
	    print("przekaznik 1(1) wlaczony")
	    requests.get(url1_on, auth = ('admin', 'admin00'))

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa +1 st. oraz mniejsza od +2 st. oraz gdy temperatura tafli jest większa/równa temperaturze "wewnątrz hali" dzielonej przez -5

	if float(hal) >= 1 and float(hal) < 2 and (float(taf_max) >= float(hal) / -5):
	    print("przekaznik 1(2) wlaczony",taf_max, " >= ", float(hal) / -5)
	    requests.get(url1_on, auth = ('admin', 'admin00'))
	    
	###### -Gdy temperatura "wewnątrz hali" jest większa/równa +2 st. oraz mniejsza od +20 st. oraz gdy temperatura tafli jest większa/równa temperaturze "wewnątrz hali" dzielonej przez -4

	if float(hal) >= 2 and float(hal) < 20 and (float(taf_max) >= float(hal) / -4):
	    print("przekaznik 1(3) wlaczony",taf_max, " >= ", float(hal) / -4)
	    requests.get(url1_on, auth = ('admin', 'admin00'))

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa +20 st. oraz gdy temperatura tafli jest większa/równa temperaturze "wewnątrz hali" dzielonej przez -3 

	if float(hal) >= 20 and (float(taf_max) >= float(hal) / -3):
	    print("przekaznik 1(4) wlaczony")
	    requests.get(url1_on, auth = ('admin', 'admin00'))



	####### WYLACZAMY PRZEKAZNIK 1 #############

	###### -Gdy temperatura "wewnątrz hali" jest mniejsza od -1st.
	if float(hal) < -1:
	    print("przekaznik 1(1) wylaczony")
	    requests.get(url1_off, auth = ('admin', 'admin00'))

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa -1 st. oraz mniejsza od +1 st. oraz temperatura na "tafli" jest mniejsza od -1.2 st.
	if float(hal) >=-1 and float(hal) < 1 and float(taf_max) < -1.2:
		print("przekaznik 1(2) wylaczony")
		requests.get(url1_off, auth = ('admin', 'admin00'))

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa +1 st. oraz mniejsza od +2 st. oraz gdy temperatura tafli jest mniejsza od temperatury ("wewnątrz hali" dzielonej przez -5)-1.2
	if float(hal) >= 1 and float(hal) < 2 and (float(taf_max) < (float(hal) / -5)-1.2):
		print("przekaznik 1(2) wylaczony", taf_max, " ")
		requests.get(url1_off, auth = ('admin', 'admin00'))

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa +2 st. oraz mniejsza od +20 st. oraz gdy temperatura tafli jest mniejsza od temperatury ("wewnątrz hali" dzielonej przez -4)-1.2
	if float(hal) >= 2 and float(hal)  < 20 and (float(taf_max) < (float(hal) / -4)-1.2):
		print("przekaznik 1(3) wylaczony", taf_max, " ")
		requests.get(url1_off, auth = ('admin', 'admin00'))

	###### -Gdy temperatura "wewnątrz hali" jest większa/równa +20 st. oraz gdy temperatura tafli jest większa/równa temperaturze ("wewnątrz hali" dzielonej przez -3)-1.2 
	if float(hal) >= 20 and (float(taf_max) < (float(hal) / -3)-1.2):
		print("przekaznik 1(4) wylaczony", float(taf_max), " >= ", (float(hal) / -3)-1.2)
		requests.get(url1_off, auth = ('admin', 'admin00'))


	roznica = float(taf_l) - float(taf_p) 
	if(abs(roznica) > 0.4 ):
	    print("przekaznik 2 wlaczony, roznica ", abs(roznica))
	    requests.get(url2_on, auth = ('admin', 'admin00'))
	elif (abs(roznica) <= 0.4 ):
	    print("przekaznik 2 wylaczony, roznica ", abs(roznica))
	    requests.get(url2_off, auth = ('admin', 'admin00'))
	   
	

import time
import requests

def full_reset():
	url1_off = 'http://192.168.111.15/stat.php?off=1'
	url2_off = 'http://192.168.111.15/stat.php?off=2'
	requests.get(url1_off, auth = ('admin', 'admin00'))
	requests.get(url2_off, auth = ('admin', 'admin00'))

if __name__ == '__main__':
    full_reset()
    while(True):
        check()
        time.sleep(170)

