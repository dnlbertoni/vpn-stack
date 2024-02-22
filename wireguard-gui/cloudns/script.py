#!/usr/bin/python
import sys
DYNAMIC_DNS_URL = "https://ipv4.cloudns.net/api/dynamicURL/?q=MzgzODcwNTo0NzE0OTI4NTY6Yjk0YTgwYmIxZTg5ODI1NmVlZmQ2NDY4NmE3Y2IzMzFiY2FlYmY3ZDNiMTM5NzBhMmQ1ODk3NDYwODc3ZTU3YQ"
if sys.version_info[0] < 3:
 import urllib
 page = urllib.urlopen(DYNAMIC_DNS_URL);
 page.close();
else:
 import urllib.request
 page = urllib.request.urlopen(DYNAMIC_DNS_URL);
 page.close();