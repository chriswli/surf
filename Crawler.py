from bs4 import BeautifulSoup
import requests

def downloadData(url):
	data_raw = requests.get(url).text
	soup = BeautifulSoup(data_raw)

# 	for link in soup.find_all('a'):
#		print link.get('href')
	
	for elem_b in soup("b"):
		print elem_b
#	print(soup.prettify())
	return 

def main(): 
	# for now, hard-code URL
	url="http://www.ndbc.noaa.gov/station_history.php?station=46221"
	downloadData(url)
	print "hello world"

if __name__ == "__main__":
	main()
	
