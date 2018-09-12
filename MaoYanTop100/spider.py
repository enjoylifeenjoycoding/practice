import json
from urllib import request, parse
import re
from multiprocessing import Pool

def open_url(url):
    # heads = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/61.0'}
    str_temp = 'http://maoyan.com/board/4?%27=&offset=' + str(url)
    req = request.Request(str_temp)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0')
    response = request.urlopen(req)

    html = response.read().decode('utf-8')

    for i in check_html(html):
        print(i)
        write_to_file(i)


def check_html(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?<img src="(.*?)".*?class="star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?="integer">(.*?)</i>.*?"fraction">(\d+).*?</dd>',
        re.S)

    items = re.findall(pattern, html)

    for item in items:
        yield {
            'index': item[0],
            'name': item[1],
            'img_url': item[2],
            'zhuyan': item[3].strip()[3:],
            'time': str(item[4]).strip()[5:],
            'pingfen': item[5] + item[6]

        }

def write_to_file(content):
    with open('/Users/yupengzhao/Desktop/result.text', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


if __name__ == '__main__':

    for i in range(10):
        pool = Pool()
        pool.map(open_url, [i * 10 for i in range(2)])

