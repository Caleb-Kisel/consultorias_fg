#python3-nmap

#os - nmap.nmap_os_detection(ip)
#service version - nmap.nmap_version_detection(ip)
#top ports - nmap.scan_top_ports(ip)
#nmap_syn_scan - nmap.nmap_syn_scan(ip)
#host discovery - nmapp.NmapHostDiscovery() results = nmap.nmap_no_portscan(ip)
import sys
import nmap3
import time

def os(ip,nmap):
	results = nmap.nmap_os_detection(ip)
	for i in results:
		print("-"*50)
		os = i['name']
		porcentaje = i['accuracy']
		print("El SO es {}\nEl porcentaje de presicion es {}".format(os,porcentaje))#resultados)

def version(ip,nmap):
	results = nmap.nmap_version_detection(ip)
	print("-"*50)
	print(ip)
	for i in results:
		protocolo = i['protocol']
		port = i['port']
		state = i['state']
		service = i['service']
		for i in service.keys():
			if "product" in i:
				producto = service['product']
			else:
				pass
			if "name" in i:
				nombre = service['name']
			else:
				pass
			if "version" in i:
				version = service['version']
			else:
				pass
		print("Protocolo => {}".format(protocolo))
		print("Puerto => {}".format(port))
		print("Estado => {}".format(state))
		print("Producto => {}".format(producto))
		print("Nombre => {}".format(nombre))
		print("Version => {}".format(version))
		print("\n")
		
def top_ports(ip,nmap):
	top_ports = nmap.scan_top_ports(ip)
	print("-"*50)
	print(ip)
	for i in top_ports['192.168.109.139']:
		protocolo = i['protocol']
		puerto = i['portid']
		estado = i['state']
		servicio = i['service']
		for i in servicio.keys():
			if "name" in i:
				nombre = servicio['name']
			else:
				pass
		print("Protocolo => {}".format(protocolo))
		print("Puerto => {}".format(puerto))
		print("Estado => {}".format(estado))
		print("Servicio => {}".format(nombre))
		print("\n")


def syn_scan(ip,nmap):
	pass

def host_descovery(ip,nmap):
	results = nmap.nmap_no_portscan(ip)
	print("-"*50)
	print(ip)
	results = results['runtime']
	results = results['summary']
	results = results.split("ress (")
	results = results[1].split(" ho")
	results = results[0]
	if results == "1":
		print("El Host esta encendido")
	elif results == "0":
		print("El Host esta apagado")
	else:
		print("Hubo un error al parsear el resultado")	

def switcher():
	modo = 3#int(input("Es momento de elegir el tipo de escaneon\n[1].OS Detection	[2].Service Version Detection	[3].Top Ports	[4].Syn Scan	[#].Salir\n=> "))
	ip = "192.168.109.139"#input("Ingresa la IP\n=> ")
	nmap = nmap3.Nmap()
	if modo == 1:
		os(ip,nmap)
	elif modo == 2:
		version(ip,nmap)
	elif modo == 3:
		top_ports(ip,nmap)
	elif modo == 4:
		syn_scan(ip,nmap)
	else:
		time.sleep(1)
		print("Saliendo...")
		sys.exit()
	pass
	#os - nmap.nmap_os_detection(ip)
	#service version - nmap.nmap_version_detection(ip)
	#top ports - nmap.scan_top_ports(ip)
	#nmap_syn_scan - nmap.nmap_syn_scan(ip)

def main():
	print("Hola, estas usando Nmap <3")
	print("Deseas [1].Escanear	[2].Host Discovery	[#].Salir")
	modo = 1#int(input("=> "))
	if modo == 1:
		switcher()
	elif modo == 2:
		ip = "192.168.109.139"#input("Ingresa la IP\n=> ")
		nmap = nmap3.NmapHostDiscovery()
		host_descovery(ip,nmap)
	else:
		sys.exit()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()