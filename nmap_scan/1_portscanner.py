import sys
import socket
from datetime import datetime

#if len(sys.argv) == 2:
#	target = socket.gethostbyname(sys.argv[1])
#else:
#	print("Invalid amount of arguments")
#	print("Syntax: python scanner.py <ip>")

target = "192.168.0.1"
#add a pretty banner
print("-"*50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET es ipv4 y SOCK_STREAM es para el puerto
		socket.setdefaulttimeout(1) # si no se conecta en 1 segundo va a pasar y continuara el escaneo
		result = s.connect_ex((target,port)) # returns un error indicator si es open 0 si no es open será 1
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit("\n")
except socket.gaierror: # cuando la ip no se puede resovler
	print("Hostname could not be resolved")
	sys.exit()
except socket.error: # para un error de socket en general
	print("Couldn't connect to server")
	sys.exit()

