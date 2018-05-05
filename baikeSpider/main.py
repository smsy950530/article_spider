from bs4 import BeautifulSoup
import url_manager
import html_downer
import html_parser
import html_outputer


class baikeSpider():

    def __init__(self):
        self.urls = url_manager.urlManger()
        self.downloader = html_downer.htmlDowner()
        self.parser = html_parser.htmlParser()
        self.outputer = html_outputer.htmlOutputer()

    def craw(self, url):
        num = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            do_url = self.urls.get_new_url()
            print(num)
            print(do_url)
            html_code = self.downloader.downloader(do_url)
            new_urls, html_cont = self.parser.parse(num, do_url, html_code)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect(html_cont)

            if num == 1000:
                break
            num = num + 1

        self.outputer.out()


if __name__ == "__main__":
    url = "https://baike.baidu.com/item/%E8%A7%A3%E9%87%8A%E5%99%A8"
    res = baikeSpider()
    res.craw(url)