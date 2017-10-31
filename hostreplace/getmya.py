# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from selenium import webdriver

import urllib
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36  Safari/601.1")
dcap["phantomjs.page.settings.userAgent"] = (
    # "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    # "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI MLA-TL10 Build/HUAWEIMLA-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36"
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko)"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)

urls_file = open('wangye_url', 'r')
urls = urls_file.readlines()
num = len(urls)

def get_a():
    index = 0
    js = 'for(var i=0;i<document.getElementsByTagName("a").length;i++){document.getElementsByTagName("a")[i].target="_blank"};'

    for url in urls:
        print "yemian url:" + url
        index = index + 1
        if index > -1:
            driver.get(url)
            driver.execute_script(js)
            time.sleep(0.5)
            content = driver.page_source
            print  "******"*10
            abiaoqians = driver.find_elements_by_tag_name("a")
            for abiaoqian in abiaoqians:
                if (abiaoqian.is_displayed()):
                    print abiaoqian.get_attribute("outerHTML")
                    winNumBeforeClick = len(driver.window_handles)
                    abiaoqian.click()
                    time.sleep(2)
                    print "click url:" + driver.current_url
                    winNumAfterClick = len(driver.window_handles)
                    if winNumAfterClick > winNumBeforeClick:
                        driver.switch_to.window(driver.window_handles[-1].current_url)
                        print "this a biaoqian xin kai chuang kou le " + driver.current_url
                        driver.close()
                        print len(driver.window_handles)
                        print driver.current_url
                    if winNumAfterClick == winNumBeforeClick:
                        urlAfterClick = driver.current_url
                        # driver.execute_script("window.history.go(-1)")
                        driver.back()
                        time.sleep(0.1)
                        driver.refresh()
                        print  "1111" + driver.current_url
                    # driver.switch_to_window(driver.window_handles[-1])
                    # print len(driver.window_handles)
                    driver.switch_to.window(driver.window_handles[-1])
                    # return driver.current_url;
                    # print driver.current_url
                    # print abiaoqian.

            # print content
            # print print_current_time()
                    time.sleep(0.1)
                else:
                    continue

    driver.close()
    driver.quit()


def print_current_time():
    timeTemp = time.time()
    timeTempNext = time.localtime(timeTemp)
    timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", timeTempNext)  # 转化为当前时间
    return timeNow



print print_current_time()


get_a()


