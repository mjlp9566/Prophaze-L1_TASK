import base64
message=input("Enter the payload to encrypt:")
message_bytes = message.encode("ascii")

base64_bytes = base64.b64encode(message_bytes)
bstr = base64_bytes.decode("ascii")


a=[str(ord((x))) for x in bstr]
enc=" ".join(a)

payload=""

for i in enc:
    payload+=hex(ord(i))+" "
print(payload)