import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from pyquery import PyQuery as pq


# browser = webdriver.Chrome()

options = Options()
options.add_argument('-headless')  # 无头参数
browser = webdriver.Firefox(executable_path='geckodriver')
wait = WebDriverWait(browser, 10)


def search():
    browser.get('http://taobao.com')

    try:
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )
        element.send_keys('美食')
        submit.click()

        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))

        get_products()
        return int(re.compile('(\d+)').search(total.text).group(1))
    except TimeoutException:
        return search()


def next_page(page_number):
    try:
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        element.clear()
        element.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
    except TimeoutException:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    # print(items)
    for item in items:
        # print('----------------------------------------------')
        # shop_temp = item.find('.shop').text()
        # if shop_temp == '南萃坊旗舰店':
        #     print(item)
        # if shop_temp == '桂花鸭旗舰店':
        #     print(item)
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
        }
        print(product)
def main():
    total = search()
    print(total)
    # for i in range(1, total + 1):
    #     next_page(i)


if __name__ == '__main__':
    main()
