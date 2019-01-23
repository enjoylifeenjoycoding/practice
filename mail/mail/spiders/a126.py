# -*- coding: utf-8 -*-
import scrapy
from mail.items import MailItem
import json

class A126Spider(scrapy.Spider):


    name = '126'
    allowed_domains = ['www.126.com', 'https://mail.126.com']
    start_urls = ['https://mail.126.com/js6/s?sid=OAhsxeUvScvHUoSitYvvCviZZryhfjNK&func=mbox:listMessages&welcome_welcomemodule_yxRecomDwon_click=1|1&LeftNavfolder1Click=1&mbox_folder_enter=1']
    parameters = {
        'sid': 'OAhsxeUvScvHUoSitYvvCviZZryhfjNK',
        'func': {'mbox': 'listMessages'},
        'welcome_welcomemodule_yxRecomDwon_click': '1|1',
        'LeftNavfolder1Click': '1',
        'mbox_folder_enter': '1',
    }
    cookie_str = 'starttime=; NTES_SESS=UGZd.hU8X5xlnGqT6EgipSCJWF49AmIq5fwZG10.cFr3ofaqo8VJbMGoGs4I.FlGDaGNHstVmx9ZlZSg2PERUiwmgvuZS1ke_67s6.Oz9Ny9_LppZI6q5yUU1DZ4G0rfAmVz0yoOsrHvkSDmRJ3cOQLe_UF4kQUxLgONOVlmgeHFAf1I0EvRhWqKVuOOO1nP.RP9MFp7smW.eyrGdkt2wLlSr; S_INFO=1537971490|0|#1&85#|zhaoyupeng1992@126.com; P_INFO=zhaoyupeng1992@126.com|1537971490|0|mail126|00&99|gud&1537970750&mail126#gud&440300#10#0#0|&0|mail126|zhaoyupeng1992@126.com; nts_mail_user=zhaoyupeng1992@126.com:-1:1; df=mail126_letter; mail_upx=c1gd.mail.126.com|c2gd.mail.126.com|c7bj.mail.126.com|c1bj.mail.126.com|c2bj.mail.126.com|c3bj.mail.126.com|c4bj.mail.126.com|c5bj.mail.126.com|c6bj.mail.126.com; mail_upx_nf=; mail_idc=; Coremail=1a7382bcf22af%OAhsxeUvScvHUoSitYvvCviZZryhfjNK%g2a14.mail.126.com; MAIL_MISC=zhaoyupeng1992@126.com; cm_last_info=dT16aGFveXVwZW5nMTk5MiU0MDEyNi5jb20mZD1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNET0Foc3hlVXZTY3ZIVW9TaXRZdnZDdmlaWnJ5aGZqTksmcz1PQWhzeGVVdlNjdkhVb1NpdFl2dkN2aVpacnloZmpOSyZoPWh0dHBzJTNBJTJGJTJGbWFpbC4xMjYuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RPQWhzeGVVdlNjdkhVb1NpdFl2dkN2aVpacnloZmpOSyZ3PWh0dHBzJTNBJTJGJTJGbWFpbC4xMjYuY29tJmw9LTEmdD0tMSZhcz10cnVl; MAIL_SESS=UGZd.hU8X5xlnGqT6EgipSCJWF49AmIq5fwZG10.cFr3ofaqo8VJbMGoGs4I.FlGDaGNHstVmx9ZlZSg2PERUiwmgvuZS1ke_67s6.Oz9Ny9_LppZI6q5yUU1DZ4G0rfAmVz0yoOsrHvkSDmRJ3cOQLe_UF4kQUxLgONOVlmgeHFAf1I0EvRhWqKVuOOO1nP.RP9MFp7smW.eyrGdkt2wLlSr; MAIL_SINFO=1537971490|0|#1&85#|zhaoyupeng1992@126.com; MAIL_PINFO=zhaoyupeng1992@126.com|1537971490|0|mail126|00&99|gud&1537970750&mail126#gud&440300#10#0#0|&0|mail126|zhaoyupeng1992@126.com; secu_info=1; mail_entry_sess=33f3bf1e090475d8ade94e8592f1e7b4ebe5549b6e5c34350a5278afe09547637824208eae462820f29c8e9e11e00014fb94a98317b25c6675b5b87346b5ce4e64cae9ecceff6d8a68ea01c0bea209f4f13947944aa5164a0b0e7a1185d91fd8e85b813f45b7bf5e6868a7b569fb4f24fce7640103c2e4bf1120ec6c105454dd92242da175b5d6a9837ac674c7689f2f0c40a2f0a69ccd965e696050ed362a2ccb182bf727ebf0594b10e7a1ea4b41b1d0860a8c899988d5d617ab771b8703ba; locale=; Coremail.sid=OAhsxeUvScvHUoSitYvvCviZZryhfjNK; mail_style=js6; mail_uid=zhaoyupeng1992@126.com; mail_host=mail.126.com; MailMasterPopupTips=1537971496452; JSESSIONID=2D0EC2AD18683B45F0B39949EA5651A0'

    def start_requests(self):
        self.cookit = self.string_for_json(self.cookie_str)
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=self.cookit,
        )

    def parse(self, response):
        if response.status != 200:
            print('请求失败{}'.format(response.status))
            return None
        print('-'*100)
        print('请求邮件列表{}'.format(response.status))
        url = 'https://mail.126.com/js6/s?sid=UBdHlHRItrcoiZcVRhIIzsFTqCwtqQhZ&func=mbox:listMessages'
        head = {
            'Referer': 'https://mail.126.com/js6/main.jsp?sid=UBdHlHRItrcoiZcVRhIIzsFTqCwtqQhZ&df=mail126_letter',
            'Host': 'mail.126.com',
            'Origin': 'https://mail.126.com',
        }
        myFormData = {
            'sid': 'UBdHlHRItrcoiZcVRhIIzsFTqCwtqQhZ',
            'func': 'mbox:listMessages',
            'welcome_welcomemodule_yxRecomDwon_click': '1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1',
            'LeftNavfolder1Click': '1',
            'mbox_folder_enter': '1',
        }
        yield scrapy.FormRequest(
            url = url,
            method='POST',
            formdata=myFormData,
            callback=self.mail_content,
            errback=self.mail_content,
            cookies=self.cookit,
            headers=head,
            dont_filter=True,
        )
        # yield scrapy.Request(
        #     url,
        #     callback=self.mail_content,
        #     cookies=self.cookit,
        #     body=myFormData,
        #     method='POST',
        #     headers=head,
        # )


    def mail_content(self, response):
        if response.status != 200:
            print('请求失败{}'.format(response.status))
            return None
        print('+'*100)
        print('列表详情{}'.format(response.status))

        data_list = response.xpath('//object')
        for item in data_list:
            print(item)
        # mail_item = MailItem()




        # data_list = response.xpath('//string[@name="subject"]/text()').extract()

        # print(data_list)
        # print(response.body.decode())
        # datas = dumps(response.body.decode())
        # print(datas)
        #datas=json.loads(response.body.decode())['content']['positionResult']['result']

    def string_for_json(self, cookie_str):
        cookie = {i.split('=')[0]: i.split('=')[1] for i in cookie_str.split('; ')}
        return cookie



