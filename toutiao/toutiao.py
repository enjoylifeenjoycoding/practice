# coding:utf8
import json
import os
import re
import ssl
from _md5 import md5
from urllib import request
from urllib.parse import urlencode

import pymongo as pymongo
import requests

from tt_db_config import *
from requests.exceptions import RequestException

ssl._create_default_https_context = ssl._create_unverified_context

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def request_Home_url(offset):
    data = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'format': 'json',
        'from': 'gallery',
        'keyword': '美女',
        'offset': offset,
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)

    try:
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 '
                                     'Firefox/61.0')
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
        return html
    except RequestException:
        print('error')
        return None


def get_page_detail(url):
    try:
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 '
                                     'Firefox/61.0')
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        return html
    except RequestException:
        print('error')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def parse_page_detail(html, url):
    title_pattern = re.compile("title:.*?'(.*?)'", re.S)
    title = re.findall(title_pattern, html)
    # print(title)

    img_pattern = re.compile(r'gallery:.JSON.parse\(.(.*?).\),', re.S)
    img_resutl = re.findall(img_pattern, html)
    if img_resutl:
        js2 = re.sub(r'\\"', '"', img_resutl[0])
        data_json = json.loads(js2)
        url_list = data_json.get('sub_images')
        urls = [re.sub(r'\\', '', item['url']) for item in url_list]
    for d_url in urls: download_image(d_url)
    return {
        'title': title[0],
        'img_urls': urls,
        'url': url
    }
    return None


def save_to_mongo(result):
    if db[MONGO_TABLE].insert_one(result):
        print('save success', result)
        return True
    return False


def download_image(url):
    try:
        req = requests.get(url)

        save_image(req.content)
    except RequestException:
        return None


def save_image(html):
    file_path = '{}/{}.{}'.format(os.getcwd(), md5(html).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(html)
            f.close()


if __name__ == '__main__':
    html = request_Home_url(0)
    for url in parse_page_index(html):
        if url is not None:
            print(url)
            html = get_page_detail(url)
            result = parse_page_detail(html, url)
            # save_to_mongo(result)
