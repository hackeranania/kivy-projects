import requests
import bs4


def get_html_data(url):
	data = requests(url)
	#return data
	
def get_covid_data():
	url = 'https://www.worldometers.info/coronavirus/'
	html_data = get_html_data(url)
	bs = bs4.Beautifulsoup(html_data.text , 'html.parser')
	print(bs)
get_covid_data()		