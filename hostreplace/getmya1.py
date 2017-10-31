#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 19:03
# @Author  : nanganglei
# @File    : getmya1.py
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

def print_current_time():
    timeTemp = time.time()
    timeTempNext = time.localtime(timeTemp)
    timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", timeTempNext)   #转化为当前时间
    return timeNow


def get_a():
    index_url = -1
    js1 = 'document.getElementById("kmap-right-container").remove()'
    js = 'for(var i=0;i<document.getElementsByTagName("a").length;i++){document.getElementsByTagName("a")[i].target="_blank"};'

    for url in urls:
        print "yemian url:" + url
        abiaoqian_kejian = 0
        abiaoqian_bukejian = 0
        index_url = index_url + 1
        if index_url > -1:
            driver.get(url)
            # driver.execute_script(js)
            # time.sleep(0.5)
            # content = driver.page_source
            print  "******"*10
            mainbody = driver.find_element_by_class_name("results")
            abiaoqians = mainbody.find_elements_by_tag_name("a")
            num_a = len(abiaoqians)
            print num_a
            index_a = 0
            xunhuancishu = 0
            print "kaishishijian:" + print_current_time()
            while index_a < num_a:
                if index_a == 89:
                    pass
                print xunhuancishu
                try:
                    current_abiaoqian = abiaoqians[index_a]
                except:
                    print "youyichangle"
                    break
                print current_abiaoqian.is_displayed()
                # print current_abiaoqian.parent()
                if current_abiaoqian.is_displayed():
                    abiaoqian_kejian = abiaoqian_kejian + 1
                    outterhtml =current_abiaoqian.get_attribute("outerHTML")
                    print 'a biao qian nei rong: ' + outterhtml
                    if ("web/uID=" in outterhtml and "sogou.com" not in outterhtml[(outterhtml.index("web/uID=")):(outterhtml[(outterhtml.index("web/uID=")):].index('"'))]) \
                            or current_abiaoqian.get_attribute("text")=="翻译此页" \
                            or ("down" in outterhtml) \
                            or ("下载" in outterhtml or "img-tag kmap-img-tag" in outterhtml):
                        # print (outterhtml.index("web/uID="))
                        # print (outterhtml.index('"'))
                        # print (outterhtml[(outterhtml.index("web/uID=")):(outterhtml.index('"'))])
                        index_a = index_a + 1
                        xunhuancishu = xunhuancishu + 1
                        continue
                    driver.implicitly_wait(0.1)
                    # driver.Manage().Timeouts().ImplicitlyWait(0.1)
                    current_abiaoqian.click()
                    time.sleep(0.1)
                    print "click url:" + driver.current_url
                    index_a = index_a + 1
                    driver.get(url)
                    time.sleep(0.2)
                    mainbody = driver.find_element_by_class_name("results")
                    abiaoqians = mainbody.find_elements_by_tag_name("a")
                    # abiaoqians = driver.find_elements_by_tag_name("a")
                else:
                    abiaoqian_bukejian = abiaoqian_bukejian + 1
                    index_a = index_a + 1
                    xunhuancishu = xunhuancishu + 1
                    continue
                    # print current_abiaoqian.get_attribute("outerHTML")

                    driver.get(url)
                    time.sleep(0.1)
                    mainbody = driver.find_element_by_class_name("results")
                    abiaoqians = mainbody.find_elements_by_tag_name("a")
                    # abiaoqians = driver.find_elements_by_tag_name("a")

                xunhuancishu = xunhuancishu + 1
            print "jie shu shi jian:" + print_current_time()
            print u"本次url的可见a标签数目是：" + str(abiaoqian_kejian)
            print u"本次url的不可见a标签数目是：" + str(abiaoqian_bukejian)
    driver.close()
    driver.quit()


def print_current_time():
    timeTemp = time.time()
    timeTempNext = time.localtime(timeTemp)
    timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", timeTempNext)  # 转化为当前时间
    return timeNow



print print_current_time()


get_a()


