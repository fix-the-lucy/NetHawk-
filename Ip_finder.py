import socket
from urllib.request import urlopen
import json

def find_local_ip():
  
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
    except Exception as e:
        return None, f"Error: {e}"

def find_public_ip():
  
    try:
        
        response = urlopen('https://api.ipify.org?format=json', timeout=5)
        data = json.loads(response.read())
        return data['ip']
    except Exception as e:
        
        try:
            response = urlopen('https://ifconfig.me/ip', timeout=5)
            return response.read().decode('utf-8').strip()
        except:
            return f"Error: Could not retrieve public IP"

def find_website_ip(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("IP Address Finder")
    print(""" Choice 1 = For local ip
Choice 2 = for global ip
Choice 3 = for Web ip
Choice 4 = To exit """)
    choose = int(input("Enter your choice :- "))
    print("=" * 50)

    if (choose == 1):
        hostname, local_ip = find_local_ip()
        print(f"1. Local Network Information:")
        print(f"   Computer Name: {hostname}")
        print(f"   Local IP Address: {local_ip}")
    elif (choose == 2):
        
        print(f"Public IP Address:")
        public_ip = find_public_ip()
        print(f"   Your Public IP: {public_ip}")
    elif ( choose == 3 ):
        
        print(f"3. Find Website IP Address:")
        domain = input("   Enter domain name (e.g., www.google.com): ")
        if domain:
            website_ip = find_website_ip(domain)
            print(f"   IP Address of {domain}: {website_ip}")
    else:
        print("Thanks for using ")

if __name__ == "__main__":
    main()
