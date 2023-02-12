import os;
ip= input('Enter the IP to scan \n')
os.system('nmap -T5 -A -v -p- -oN nmapscan_'+ ip);
os.system("gobuster dns -w /usr/share/amass/wordlists/subdomains-top1mil-20000.txt -t 200 -o domainenum.txt -d" + ip);
os.system("gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 200 -o direnum.txt -u" + ip);
