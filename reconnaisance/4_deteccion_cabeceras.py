import requests
import argparse
import sys

parse = argparse.ArgumentParser(description="Detector de Cabeceras")
parse.add_argument('-t','--target',help="Objetivo")
parse = parse.parse_args()

def main():
	if parse.target:
		try:
			url = requests.get(url=parse.target)
			cabeceras = dict(url.headers)
			for cabecera in cabeceras:
				print(cabecera+" : "+cabeceras[cabecera])
		except:
			print("No se pudo establecer la conexion")
	else:
		print("No hay objetivo definido")



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()