from bs4 import BeautifulSoup
import requests


print('[~] Collecting Companies ...\n\n')
for z in range(200):
	print('\n\t[!] Scrapping Page '+str(z))
	res=requests.get('https://themanifest.com/in/web-development/companies?page='+str(z))
	fres=res.text

	soup = BeautifulSoup(fres,'lxml')


	all=soup.find_all('h3',class_='text-uppercase title lines1')
	names=[]
	for x in all:
		names.append(x.a.text.strip())


	all=soup.find_all('span',class_='rating-overall-value')
	ratings=[]
	for x in all:
		ratings.append(x.text.strip())


	all=soup.find_all('div',class_='profile-visit')
	websites=[]
	for x in all:
		websites.append(x.a['href'])


	all=soup.find_all('span',class_='comp-addr')
	city=[]
	for x in all:
		city.append(x.span.text.strip())


	for i in range(len(names)):
		with open('records.txt','a+') as fh:
			fh.write(names[i]+','+ratings[i]+','+city[i]+','+websites[i]+'\n')
