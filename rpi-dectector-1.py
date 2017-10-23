import nmap
import json


rpi_ip_list = []
rpi_name_list = []


def pi_search():
	print ('Searching for RPi')
	print ("---------------------------")

	nm = nmap.PortScanner()
	nm.scan('192.168.1.0/24',arguments='-sP') #Note that I tested with -sP to save time
	for host in nm.all_hosts():
	  #print(host + " "+nm[host].hostname())
	  item = nm[host]['addresses']
  	  if nm[host].hostname() == 'raspberrypi' :
            print (nm[host].hostname(),item)

	print ("---------------------------")

def main():

	if rpi_ip_list == []:
		print ('Running nmap')
		pi_search()
		#need to do some works to display correctly

if __name__ == "__main__":
    main()
