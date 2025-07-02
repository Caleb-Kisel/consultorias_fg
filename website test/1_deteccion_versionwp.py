import requests
import sys
from bs4 import BeautifulSoup

def main():
	url = "https://anormalix.com"#input("Porfavor ingresa la URL del sitio web\n=> ")
	cabecera = {'User-Agent':'Firefox'}
	peticion = requests.get(url=url,headers=cabecera)
	soup = BeautifulSoup(peticion.text,'html.parser')
	for v in soup.find_all('meta'):
		if v.get('name') == 'generator':
			version = v.get('content')
			print(version)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()