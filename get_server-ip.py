print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program")


import socket
url= input("Enter Host:")
print("IP:",socket.gethostbyname(url))