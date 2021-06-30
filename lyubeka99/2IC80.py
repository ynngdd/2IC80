import requests
import hashlib
from bs4 import BeautifulSoup

session = requests.session() # USE TO ESTABLISH SESSION 

resp = session.get("http://206.189.20.127:31752") # HTTP GET (OVER THE SESSION)
text = resp.text
array = text.split("<")
print(array[9])
code = array[9][-20:] # CONTAINS THE STRING WE WISH TO ENCODE
print(code)

encrypted = hashlib.md5(code.encode('utf-8')) # MD5 ENCRYPTION

final = encrypted.hexdigest()

print(final) 

data = {'hash': final}

final_final = session.post(url="http://206.189.20.127:31752", data = data) # HTTP POST (OVER THE SESSION AGAIN)

print(final_final.text)
