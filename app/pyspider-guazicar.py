#!/Users/kevin/Workspace/.pyenvs/py-scraper/bin python
# -*- encoding: utf-8 -*-
# Created on 2016-05-01 11:31:38
# Project: guazi

"""
TODO: imbed mongo
"""

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    client = pymongo.MongoClient('mongodb://kevin:1234@localhost:27017/guazi2')
    guazi2 = client['guazi2']
    car = guazi2['car']

    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.guazi.com/bj/buy', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc(
                'body > div.header > div.hd-top.clearfix > div.c2city > div > div > dl > dd > a').items():
            self.crawl(each.attr.href, callback=self.second_page)

    @config(age=10 * 24 * 60 * 60)
    def second_page(self, response):
        num = int(response.doc('div.seqBox.clearfix > p > b').text())
        urls = [response.url + 'o{}/'.format(str(i)) for i in range(1, num / 40 + 2, 1)]
        for each in urls:
            self.crawl(each, callback=self.third_page)

    @config(age=10 * 24 * 60 * 60)
    def third_page(self, response):
        for each in response.doc('div.list > ul > li > div > a').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc(
                'body > div.w > div > div.laybox.clearfix > div.det-sumright.appoint > div.dt-titbox > h1').text(),
            "address": response.doc(
                'body > div.w > div > div.laybox.clearfix > div.det-sumright.appoint > ul > li:nth-child(5) > b').text(),
            "cartype": response.doc(
                'body > div.w > div > div.laybox.clearfix > div.det-sumright.appoint > ul > li:nth-child(3) > b').text(),
            "price": response.doc(
                'body > div.w > div > div.laybox.clearfix > div.det-sumright.appoint > div.basic-box > div.pricebox > span.fc-org.pricestype > b').text().replace(
                u'¥', ''),
            "region": response.doc('#base > ul > li.owner').text()
        }

    def on_result(self, result):
        self.car.insert_one(result)
