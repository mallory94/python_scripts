import requests
import re
from bs4 import BeautifulSoup

url = "http://www.httptunnel.ge/ProxyListForFree.aspx"

response = requests.get(url)

#print(response)

if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        proxies = soup.select('td a')
        #print(proxies)

        for proxy in proxies:
            match = re.search(".*HyperLink.*", str(proxy))
            if match:
                print(proxy.text)
