import sys
import socket
from datetime import datetime

def main():
	target = "192.168.109.140"

	print("-"*50)
	print("El target es : " + target)
	print("Inicio de escaneo: " +str(datetime.now()))
	print("-"*50)

	for port in range(1,81):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("El puerto {} se encuentra abierto".format(port))
		s.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()