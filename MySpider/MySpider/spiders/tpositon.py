# -*- coding: utf-8 -*-
import scrapy
import json
from MySpider.items import MyspiderItem


# add remark
# fix 2
class TpositonSpider(scrapy.Spider):
    name = 'tpositon'
    allowed_domains = ['tencent.com']
    url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1558690732373&pageIndex=%s&pageSize=10"
    offset = 1
    start_urls = [url % offset]

    def parse(self, response):
        if response.status == 200:
            keys = ["Id", "PostId", "RecruitPostId", "PostURL"]
            json_data = json.loads(response.text)
            json_data = json_data["Data"]["Posts"]
            for l in json_data:
                data = {}
                for key, value in l.items():
                    if key not in keys:
                        data[key] = value
                yield data
            if self.offset < 10:
                self.offset += 1
            nexturl = self.url % self.offset
            yield scrapy.Request(nexturl, callback=self.parse)
