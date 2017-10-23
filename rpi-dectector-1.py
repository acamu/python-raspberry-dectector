#import os
#import platform
#import re
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
          if 'mac' in nm[host]['addresses']:
            print('mac address found: {}'.format(nm[host]['addresses']))
            print('vendor: {}'.format(nm[host]['vendor']))

	print ("---------------------------")

def main():

	if rpi_ip_list == []:
		print ('Running nmap')
		pi_search()


if __name__ == "__main__":
    main()
