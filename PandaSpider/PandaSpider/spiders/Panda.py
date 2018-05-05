# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.http import Request
from urllib import parse
import re
import time

from selenium import webdriver
from PandaSpider.items import PandaItem
from PandaSpider.util.common import get_md5

class PandaSpider(scrapy.Spider):
    name = 'Panda'
    allowed_domains = ['www.panda.tv']
    start_urls = ['https://www.panda.tv/all']

    def parse(self, response):
        self.num = 1
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)
        bowser = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe", chrome_options=chrome_opt)
        bowser.get(response.url)
        time.sleep(5)
        new_html_urls = []
        i = 1
        html_click_num = bowser.find_element_by_xpath('//*[@id="pages-container"]/div/div/a[7]').text
        while i < 2:
            i+=1
            time.sleep(1)
            html_code = bowser.page_source
            html_urls = re.findall('href="/(\d+)|(https://xingyan.panda.tv/\d+)"', html_code)

            for html_url in html_urls:
                if "xingyan" in html_url[1]:
                    html_url = html_url[1]
                    new_html_urls.append(html_url)

                else:
                    html_url = html_url[0]
                    new_html_urls.append(parse.urljoin(response.url, html_url))

            print(new_html_urls)
            bowser.find_element_by_css_selector(".j-page-next").click()
        bowser.close()
        for html_url in new_html_urls:
            yield Request(url=html_url, callback=self.parse_detail)

    def parse_detail(self, response):
        time.sleep(2)
        panda = PandaItem()
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)

        bowser = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe", chrome_options=chrome_opt)
        bowser.get(response.url)
        title = bowser.find_element_by_class_name("room-head-info-title").text
        name = bowser.find_element_by_class_name("room-head-info-hostname").text
        follow_count = bowser.find_element_by_class_name("room-head-tool-follow-count").text.replace(",","")
        num = bowser.find_element_by_css_selector(".room-viewer-main>span").text.replace(",","")
        room_id = re.findall(".*?(\d+)",response.url)[0]
        html_url = response.url
        has_id = get_md5(response.url)

        panda["title"] = title
        panda["name"] = name
        panda["follow_count"] = follow_count
        panda["num"] = num
        panda["room_id"] = room_id
        panda["html_url"] = html_url
        panda["has_id"] = has_id
        bowser.close()
        print(self.num)
        self.num = self.num + 1

        yield panda


        pass
