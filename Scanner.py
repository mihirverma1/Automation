import os;

ip= input('Enter the IP to scan \n')
os.system('nmap -T5 -A -v -p- -oN nmapscan_'+ ip)
