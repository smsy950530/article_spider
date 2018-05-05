# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from ArticleSpider.items import LagouItemLoader,LagouItem
from datetime import datetime
from ArticleSpider.util.common import get_md5
import time
import re

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']
    rules = (
        Rule(LinkExtractor(allow=r'/jobs/\d+.html'), callback='parse_item', follow=True),
    )

    bowser = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe")
    bowser.get("https://passport.lagou.com/login/login.html")
    bowser.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[1]/input").send_keys("18xxxxxxx")
    bowser.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[2]/input").send_keys("syxxxxxxx")
    bowser.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[5]/input").click()
    time.sleep(10)
    cookies = bowser.get_cookies()
    print(cookies)
    cookie_dict = {}
    import pickle
    for cookie in cookies:
        f = open("G:/pythonSaveWorld/ArticleSpider/ArticleSpider/cookies/lagou/" + cookie["name"] + ".lagou", "wb")
        pickle.dump(cookie, f)
        f.close()
        cookie_dict[cookie["name"]] = cookie["value"]
    bowser.close()

    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': cookie_dict,
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def parse_item(self, response):
        lagou = LagouItemLoader(item=LagouItem(), response=response)
        lagou.add_css("title", ".job-name span::text")
        lagou.add_css("job_desc", ".job_bt div")
        lagou.add_xpath("job_need", "/html/body/div[2]/div/div[1]/dd/p[1]/span[4]/text")

        lagou.add_css("job_tag", ".position-label.clearfix")
        lagou.add_css("company_name", ".b2::attr(alt)")
        lagou.add_css("company_addr", ".work_addr")
        lagou.add_value("crawl_time", datetime.now())
        lagou.add_value("url_object_id", get_md5(response.url))
        job_item = lagou.load_item()

        return job_item
