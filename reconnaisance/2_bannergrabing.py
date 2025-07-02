import socket
import sys

def banner(ip,puerto):
	s = socket.socket()
	s.connect((ip,puerto))
	print(str(s.recv(1024)))


def main():
	ip = "192.168.109.140"#input("Ingresa la ip objetivo: ")#"192.168.109.140"
	port = 21#int(input("Ingresa el puerto: "))#21
	banner(ip,port)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt():
		sys.exit()