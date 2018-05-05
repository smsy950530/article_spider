import json
import MySQLdb

class htmlOutputer():
    def collect(self, html_cont):
        # 将其保存为json文件
        with open("G:/pythonSaveWorld/baikeSpider/collect.json", "a", encoding="utf-8") as f:
            json.dump(html_cont, f, ensure_ascii=False, indent=" ")

        # con = MySQLdb.connect(
        #     host = "127.0.0.1",
        #     user = "shenyu",
        #     passwd = "950530",
        #     db = "baike",
        #     charset = "utf8"
        #
        # )
        # num = html_cont["num"]
        # title = html_cont["title"]
        # main = html_cont["main"]
        # url = html_cont["url"]
        # insert_sql = """
        #     insert into baike_spider(num, title, content, url) VALUES (%s, %s, %s, %s)
        # """
        #
        # cursor = con.cursor()
        # cursor.execute(insert_sql, (num, title, main, url))


    def out(self):
        pass