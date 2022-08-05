import requests
#payload=input("Enter the payload")
#hostname=input("Enter the IP:")      #IF THERE IS A DNS SERVER CONFIGURED IN THE NETWORK THEN WE CAN DIRECTLY ENTER THE HOSTNAME OTHERWISE WE HAVE TO GIVE THE IP OF THE SERVER

hostname="localhost"
port=str(7878)
url="http://"+hostname+":"+port
payload="0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38"
#payload="0x3839203530203730203438"
try:
 x=requests.post(url,data=payload)
 print(x.text)
except:
 print("Check IP of the sever (or) The server may not be active")




