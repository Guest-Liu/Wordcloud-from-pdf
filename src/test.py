import requests
r = requests.get("http://www.baidu.com")
r.text[:100]
