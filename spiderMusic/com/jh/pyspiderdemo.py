#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-11 11:06:14
# Project: getallqiushi

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.qiushibaike.com/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        list = response.doc(".pagination li a").items()
        
        for tag in  list:
            print tag.attr.href
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
