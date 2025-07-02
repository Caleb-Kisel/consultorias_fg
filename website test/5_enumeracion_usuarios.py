import sys
import json
import requests
from bs4 import BeautifulSoup

def main():
	url = "http://www.arturo-alvarez.com"
	peticion = requests.get(url+"/wp-json/wp/v2/users")
	with open('json.txt','wb') as file:
		file.write(peticion.content)

	with open('json.txt') as json_file:
		for u in json.load(json_file):
			user = u['slug']
			print(user)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()