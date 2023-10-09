import os;
ip= input('Enter the IP to scan \n')
os.system('nmap -sS -sC -sV -oA nmap -v '+ ip);
os.system("gobuster vhost -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -t 50 --append-domain -u" + ip);
os.system("gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -o direnum.txt -u" + ip);
