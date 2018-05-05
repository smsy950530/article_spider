from bs4 import BeautifulSoup
import re
from urllib import parse


class htmlParser():
    def get_urls(self, do_url, soup):
        new_urls = set()
        # self.soup.find_all("a", href=re.findall(r'/item/[\w%]+'))
        links = re.findall('/item/[\w%]+', str(soup))
        for link in links:
            new_url = link
            new_url_full = parse.urljoin(do_url, new_url)
            new_urls.add(new_url_full)
        return new_urls

    def get_main(self, num, do_url, soup):

        html_cont = {}
        try:
            html_title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title")
            html_title = html_title_node.get_text().strip()
        except:
            html_title = "存在拼音"

        try:
            html_main_node = soup.find("div", class_="lemma-summary")
            html_main = html_main_node.get_text().strip()
        except:
            html_main = "不存在"
        html_cont["num"] = num
        html_cont["title"] = html_title
        html_cont["main"] = html_main
        html_cont["url"] = do_url
        return html_cont

    def parse(self, num, do_url, html_code):
        if html_code is None:
            return
        soup = BeautifulSoup(html_code, "html.parser")
        new_urls = self.get_urls(do_url, soup)
        html_main = self.get_main(num, do_url, soup)
        return new_urls, html_main