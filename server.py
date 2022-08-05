from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import base64

def remove_0x(payload):
    str1=payload
    newch=""
    str2= ''
    for i in range(len(str1)):
       if((str1[i]=='0' and str1[i+1]=='x') or str1[i]=='x' or str1[i]==" "):
         str2=str2+newch
       else:
        str2=str2+str1[i]
    return str2


def hexToASCII(hex):
	ascii=""
	for i in range(0,len(hex),2):
		part=hex[i:i+2]
		ch=chr(int(part, 16))
		ascii+=ch
	return ascii

def AsciiToChr(ASCII):
    a=ASCII.split(" ")
    a=[chr(int(x)) for x in a]
    return "".join(a)

def base64decode(message):
    return base64.b64decode(message)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length=int(self.headers['Content-Length'])
        body=self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response=BytesIO()
        payload=remove_0x(body.decode('ascii'))      #removed 0x and spaces

        response.write(b'Encoded Payload:')
        response.write(bytes(payload,'ascii'))

        hex_decoded_payload=hexToASCII(payload)            #decoded from hex (ascii values)
        ascii_decoded_payload=AsciiToChr(hex_decoded_payload)      #decoded from ascii (characters) 
        message=base64decode(ascii_decoded_payload)

        response.write(b'\nDecoded Payload:')
        response.write(message)
        self.wfile.write(response.getvalue())
        
with HTTPServer(('', 7878),handler) as server:
    print("SERVER STARTED")
    server.serve_forever()
