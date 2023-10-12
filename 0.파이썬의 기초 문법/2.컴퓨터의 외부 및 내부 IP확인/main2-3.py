
# import requests
# import re
# req = requests.get("http://ipconfig.kr")
# out_addr = re.search(r'IP Address:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)
# print(out_addr)

import requests
import re

try:
    req = requests.get("http://ipconfig.kr")
    if req.status_code == 200:
        out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)
        if out_addr:
            print("IP Address:", out_addr.group(1))
            print(type(out_addr))
        else:
            print("IP Address not found in the response.")
    else:
        print(f"Failed to retrieve the web page. Status code: {req.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
