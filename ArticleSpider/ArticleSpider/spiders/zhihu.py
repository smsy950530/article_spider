# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from scrapy.http import Request
from scrapy.selector import Selector


# class ZhihuSpider(scrapy.Spider):
#     name = 'zhihu'
#     allowed_domains = ['www.zhihu.com/signup']
#     start_urls = ['http://www.zhihu.com/signup/']
#
#     bowser = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe")
#     bowser.get("https://www.zhihu.com/signup")
#     bowser.find_element_by_css_selector(".SignContainer-switch span").click()
#     bowser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys("13xxxxxx")
#     bowser.find_element_by_css_selector(".SignFlow-password .SignFlowInput .Input-wrapper input").send_keys("syxxxxxxx")
#     bowser.find_element_by_css_selector(".Button.SignFlow-submitButton.Button--primary.Button--blue").click()
#     time.sleep(5)
#     bowser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage = document.body.scrollHeight;return lenOfPage;)")
#
#     def parse(self, response):
#
#         pass
