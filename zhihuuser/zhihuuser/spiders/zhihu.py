# -*- coding: utf-8 -*-
import scrapy
from zhihuuser.items import UserItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/li-lao-shu/following']

    def start_requests(self):
        cookies_url = '_zap=2c55bfd5-815c-45c2-916e-81514e25e32a; d_c0="AIBkhq2_Cw6PTnl_OFoQgK_IV52fafmXwY4=|1534086613"; _xsrf=kyE3r4CQEwPk2xLRhAw05d1LfOSnkxha; q_c1=fb28649b273740e2a3f0c41f2e6a36b0|1537117255000|1534086615000; tst=r; l_n_c=1; l_cap_id="NzNiZGVhMDQzMmY5NGNmN2FjMWU0ZmRjNTIwNTRlMjA=|1537513722|113e320e900c989843e7b82b9f52e01bca5dd94b"; r_cap_id="M2NkNWUwODcwNWNhNDA0N2IwZTRmYjc2NmM1YTZmODQ=|1537513722|4c8ca0a0209d6fc49644b05fedc26e4ffb2bd450"; cap_id="YmVhNjQ0OTJlNzcxNGQ0Zjg4MmQ1NDU2YjNhZGU5YTE=|1537513722|0032647a4f3548e9d30e52dbec4c8e49e80e274c"; n_c=1; __utma=51854390.660320361.1535620508.1535620508.1537513725.2; __utmc=51854390; __utmz=51854390.1537513725.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/zhao-yu-peng/following; __utmv=51854390.000--|2=registration_date=20131120=1^3=entry_date=20180812=1; capsion_ticket="2|1:0|10:1537513971|14:capsion_ticket|44:YjI2MzM3ZGYxYzhiNDJlMmEwMDllODRhMGIyY2I0MjE=|0ef19ca10836fb7dcb72c4b82515ce6ce20e4a80971e65539cf3b48f788d1bf2"; z_c0="2|1:0|10:1537513983|4:z_c0|92:Mi4xMkRBakFBQUFBQUFBZ0dTR3JiOExEaVlBQUFCZ0FsVk5fLWVSWEFCZ2VSbzliVHNXYjVHT1RHZjZ5dDlESWNfMHhR|d4e5c65700c7124da756ce634b341413f8e06a2c4c990b274b534374c3da9df1"; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186'
        cookies_dict = {i.split('=')[0]:i.split('=')[1] for i in cookies_url.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict,
        )

    def parse(self, response):
        print('-'*100)
        self.userItem = UserItem()
        self.userItem['name'] = response.xpath('//span[@class="ProfileHeader-name"]/text()').extract_first()
        self.userItem['profession'] = response.xpath('//span[@class="RichText ztext ProfileHeader-headline"]/text()').extract_first()
        self.userItem['img_head_url'] = response.xpath('//div[@class="UserAvatar ProfileHeader-avatar"]/img/@src').extract_first()
        # self.userItem['attention'] = response.xpath('//div[@class="NumberBoard"]').extract_first()
        temp = response.xpath('//div[@class="NumberBoard-itemInner"]')
        print(self.userItem)

