# # -*- coding: utf-8 -*-
# import scrapy
# from selenium import webdriver
# import time
#
# class WeiboSpider(scrapy.Spider):
#     name = 'weibo'
#     allowed_domains = ['www.weibo.com']
#     start_urls = ['http://www.weibo.com/']
#
#     bowser = webdriver.Chrome(executable_path="D:/chromedriver/chromedriver.exe")
#     bowser.get("http://www.weibo.com/")
#     time.sleep(5)
#     bowser.find_element_by_css_selector(".info_list.username .input_wrap input").send_keys("13xxxxx")
#     bowser.find_element_by_css_selector(".info_list.password .input_wrap input").send_keys("syxxxxxxx")
#     bowser.find_element_by_css_selector(".W_btn_a.btn_32px").click()
#     def parse(self, response):
#         pass
