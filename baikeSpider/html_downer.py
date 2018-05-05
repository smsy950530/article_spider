from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import quote
import re


class htmlDowner():
    def getStatusCode(self,url):
        r = requests.get(url, allow_redirects=False)
        return r.status_code

    def downloader(self, url):
        check = re.compile(u'[\u4e00-\u9fa5]+')
        match = check.search(url)
        if match:
            url = quote(url, safe='/:?=')
        else:
            url = url
        response = urllib.request.urlopen(url)
        res = response.read()
        html = res.decode("utf8")
        res_code = self.getStatusCode(url)
        if res_code == 302 or res_code == 200:
            return html
        else:
            return None



