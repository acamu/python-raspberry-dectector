# python-raspberry-dectector

I used this page for exemple
from : https://github.com/TranceCat/Raspberry-Pi-orchestration


[Pre requisites]

    Execute the cmd with sudo 

## Install pytho-pip

    sudo yum install python-pip
    sudo pip install --upgrade pip

## Install python nmap

    pip install python-nmap
    
    
## Execute

    # with sudo without nmap doesn't work correctly
    sudo python detector-1.py


# Thing to know

If you want the mac address you must be on the same lan than the raspberry otherwise you will retrieve only the IP.
It's enough to connect to the pi :)
