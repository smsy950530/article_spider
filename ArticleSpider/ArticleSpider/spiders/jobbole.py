# # -*- coding: utf-8 -*-
# import scrapy
# from urllib import parse
# from scrapy.http import Request
# from scrapy.loader import ItemLoader
#
# from ArticleSpider.items import Artcilespidertest,ArticleItemLoader
# import re
#
# class JobboleSpider(scrapy.Spider):
#     name = 'jobbole'
#     allowed_domains = ['blog.jobbole.com']
#     start_urls = ['http://blog.jobbole.com/all-posts/']
#
#     def parse(self, response):
#         html_nodes = response.css("#archive .post-thumb a")
#         for html_node in html_nodes:
#             html_url = html_node.css('::attr(href)').extract_first()
#             image_url = html_node.css('img::attr(src)').extract_first()
#             yield Request(url=parse.urljoin(response.url, html_url), meta={"image_url": image_url}, callback=self.parse_detail)
#
#         next_url = response.css(".navigation.margin-20 .next.page-numbers::attr(href)").extract_first()
#         if next_url:
#             yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
#
#     def parse_detail(self,response):
#         article = Artcilespidertest()
#         title = response.css('.entry-header h1::text').extract_first()
#         image_url = response.meta["image_url"]
#         id = re.findall('.*?(\d+)', response.url)[0]
#         # node = response.css('.entry-meta p')
#         # date = node.css('::text')[0].extract().strip().replace('·', '').strip()
#         # tag = node.css('a::text').extract_first()
#         # zan = response.css('.post-adds h10::text').extract_first()
#         # zan_num = re.match('(\d*).*', zan).group(1)
#         # if zan_num:
#         #     zan_num = int(zan_num)
#         # else:
#         #     zan_num = 0
#         # shoucang = response.xpath('//*[@class="post-adds"]/span[2]/text()').extract_first()
#         # shoucang_num = re.match('(\d*).*', shoucang).group(1)
#         # if shoucang_num:
#         #     shoucang_num = shoucang_num
#         # else:
#         #     shoucang_num = 0
#         # pinglun = response.css('.post-adds a span::text ').extract_first()
#         # pinglun_num = re.match('(\d*).*', pinglun).group(1)
#         # if pinglun_num:
#         #     pinglun_num = int(pinglun_num)
#         # else:
#         #     pinglun_num = 0
#         # content = response.css('.entry').extract()
#
#         item_loader = ArticleItemLoader(item=Artcilespidertest(), response=response)
#         item_loader.add_css("title", ".entry-header h1::text")
#         item_loader.add_css("date", ".entry-meta p::text")
#         item_loader.add_css("tag", ".entry-meta p a::text")
#         item_loader.add_css("zan_num", ".post-adds h10::text")
#         item_loader.add_xpath("shoucang_num", "//*[@class='post-adds']/span[2]/text()")
#         item_loader.add_css("pinglun_num", ".post-adds a span::text")
#         item_loader.add_css("content", ".entry")
#         item_loader.add_value("html_url", response.url)
#         item_loader.add_value("image_url", [image_url])
#         item_loader.add_value("article_id", id)
#
#         article = item_loader.load_item()
#         yield article
#
#         pass
