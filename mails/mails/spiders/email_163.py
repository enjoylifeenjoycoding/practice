# -*- coding: utf-8 -*-
import os

import scrapy
from mails.items import MailsItem
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

class Email163Spider(scrapy.Spider):
    name = 'email_163'
    allowed_domains = ['https://mail.126.com/']
    start_urls = [
        'https://mail.126.com/js6/s?sid=OAhsxeUvScvHUoSitYvvCviZZryhfjNK&func=mbox:listMessages',  # 邮件列表
    ]

    email_username = 'zhaoyupeng1992'
    email_password = '599258047'

    def login_email(self):
        try:
            options = webdriver.ChromeOptions()

            options.set_headless()

            browser = webdriver.Chrome(chrome_options = options)

            browser.get(self.allowed_domains[0])

            sleep(3)

            browser.switch_to.frame('x-URS-iframe')

            browser.find_element_by_name("email").send_keys(self.email_username)

            browser.find_element_by_name("password").send_keys(self.email_password)

            browser.find_element_by_id('dologin').click()

            sleep(5)
            cookielist = browser.get_cookies()

            cookie = [item.get('name') + "=" + item.get('value') for item in cookielist]
            cookiestr = '; '.join(item for item in cookie)
            # print(cookiestr)
            return cookiestr
        except TimeoutException:
            print('请求超时')
            return None

    def start_requests(self):
        '''邮件列表'''
        self.cookies = {'mail_uid': 'zhaoyupeng1992@126.com', 'Coremail.sid': 'OAMCzJUvwfhHUoWKCYvvIChlWmyBtpmK', 'locale': '', 'JSESSIONID': '106044E29134E968CB37258E1817233A', 'secu_info': '1', 'mail_host': 'mail.126.com', 'MAIL_PINFO': 'zhaoyupeng1992@126.com|1538061006|0|mail126|00&99|gud&1538060845&mail126#gud&440300#10#0#0|&0|mail126|zhaoyupeng1992@126.com', 'MAIL_SINFO': '1538061006|0|#1&85#|zhaoyupeng1992@126.com', 'cm_last_info': 'dT16aGFveXVwZW5nMTk5MiU0MDEyNi5jb20mZD1odHRwcyUzQSUyRiUyRm1haWwuMTI2LmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNET0FNQ3pKVXZ3ZmhIVW9XS0NZdnZJQ2hsV215QnRwbUsmcz1PQU1DekpVdndmaEhVb1dLQ1l2dklDaGxXbXlCdHBtSyZoPWh0dHBzJTNBJTJGJTJGbWFpbC4xMjYuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RPQU1DekpVdndmaEhVb1dLQ1l2dklDaGxXbXlCdHBtSyZ3PWh0dHBzJTNBJTJGJTJGbWFpbC4xMjYuY29tJmw9LTEmdD0tMSZhcz10cnVl', 'mail_style': 'js6', 'starttime': '', 'mail_upx': 'c2gd.mail.126.com|c1gd.mail.126.com|c4bj.mail.126.com|c5bj.mail.126.com|c6bj.mail.126.com|c7bj.mail.126.com|c1bj.mail.126.com|c2bj.mail.126.com|c3bj.mail.126.com', 'Coremail': '046840f53d625%OAMCzJUvwfhHUoWKCYvvIChlWmyBtpmK%g2a14.mail.126.com', 'NTES_SESS': 'Dkmvr1Hnq0hq8WzCwO72339GrLNAxfS_qWUjJyfOZEc6uWdmu57zsxJuJGBQOErJhdJ_TGn7a9ljrjvP0tXAD8UaPIgjvyR2M13G1Oepl_w9U7EOLg9BlyDDyhjBJfcWFa7pfwueGcTIRvhaAz6ZeLi2MDEBRLD9iPe_e7raP2TEFWyQfXIAKNmq7geeey4tOAtlxEC3GaNO2wcJ.Rn0Uirvc', 'mail_idc': '', 'mail_upx_nf': '', 'MAIL_SESS': 'Dkmvr1Hnq0hq8WzCwO72339GrLNAxfS_qWUjJyfOZEc6uWdmu57zsxJuJGBQOErJhdJ_TGn7a9ljrjvP0tXAD8UaPIgjvyR2M13G1Oepl_w9U7EOLg9BlyDDyhjBJfcWFa7pfwueGcTIRvhaAz6ZeLi2MDEBRLD9iPe_e7raP2TEFWyQfXIAKNmq7geeey4tOAtlxEC3GaNO2wcJ.Rn0Uirvc', 'df': 'mail126_letter', 'mail_entry_sess': '802c9e91284dea44b537eafab6439e733f8bd010c31d2cc18df7c32b67b4abd3f81a6832bd1fed1d0af1929f5ba9465508819ec805b4881445fcb94aaa5588667fd074c05762aad9a32ac8e86c9bd3820e2b39ac31e7fae8a992932be6725f6bff770572b9166667d8b94c03eb35735bb7e1bfa34e4e34c6e59ec6045d0b75e2b1ffc7ab97a5aaeab93aad17e457d48e63b99a0f75a5e336c08161a56d9a8c734430adefd0d11d91b49867316f7293c6df3ff56ad73cb16bffff59463c359766', 'MAIL_MISC': 'zhaoyupeng1992@126.com', 'nts_mail_user': 'zhaoyupeng1992@126.com:-1:1', 'P_INFO': 'zhaoyupeng1992@126.com|1538061006|0|mail126|00&99|gud&1538060845&mail126#gud&440300#10#0#0|&0|mail126|zhaoyupeng1992@126.com', 'S_INFO': '1538061006|0|#1&85#|zhaoyupeng1992@126.com'}
        # self.cookies = self.string_for_json(self.login_email())
        if self.cookies == None:
            return None
        self.sid=self.cookies.get('Coremail.sid')
        # print(self.cookies)
        print('成功获取登陆cookie 开始获取邮件列表')

        yield scrapy.Request(
            url='https://mail.126.com/js6/s?sid={}&func=mbox:listMessages'.format(self.sid),
            cookies=self.cookies,
            dont_filter=True,
            callback=self.parse,
        )

    def parse(self, response):
        '''解析邮件列表'''
        if response.status == 200:
            mail_list = response.xpath('//array/object')
            print('成功请求邮件列表邮件数量：{}'.format(len(mail_list)))
            for item in mail_list[0:30]:

                mail_item = MailsItem()
                mail_item['mail_id'] = item.xpath('./string[@name="id"]/text()').extract_first()
                mail_item['mail_from'] = item.xpath('./string[@name="from"]/text()').extract_first()
                mail_item['mail_to'] = item.xpath('./string[@name="to"]/text()').extract_first()
                mail_item['mail_subject'] = item.xpath('./string[@name="subject"]/text()').extract_first()
                mail_item['mail_sentDate'] = item.xpath('./date[@name="sentDate"]/text()').extract_first()
                mail_item['mail_receivedDate'] = item.xpath('./date[@name="receivedDate"]/text()').extract_first()
                mail_item['mail_priority'] = item.xpath('./int[@name="priority"]/text()').extract_first()
                mail_item['mail_backgroundColor'] = item.xpath('./int[@name="backgroundColor"]/text()').extract_first()

                print(mail_item['mail_subject'])

                # 请求邮件内容
                yield scrapy.Request(
                    url='http://mail.126.com/js6/read/readhtml.jsp?mid={}&font=15&color=138144'.format(
                        mail_item['mail_id']),
                    callback=self.mail_content,
                    # errback=self.mail_content,
                    meta=mail_item,
                    dont_filter=True
                )

        else:
            print('请求失败 {}'.format(response.status))

    def mail_content(self, response):
        print('-' * 100)
        print('邮件详情')
        item = response.meta
        if response.status == 200:
            body_html = response.xpath('//body').extract_first()
            file_path = '{}/{}.html'.format(os.getcwd(), item['mail_id'])
            print('保存文件：{}'.format(file_path))
            with open(file_path, 'w') as f:
                f.write(body_html)
                f.close()
            if body_html == None:
                return None
            else:
                pass
        else:
            print('error')

    def string_for_json(self, cookie_str):
        '''cookie字符串转字典'''
        if cookie_str == None:
            return None
        cookie = {i.split('=')[0]: i.split('=')[1] for i in cookie_str.split('; ')}
        return cookie
