#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 17:41
# @Author  : nanganglei
# @File    : pageDetect1.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 16:04
# @Author  : nanganglei
# @File    : pageDetect.py

from selenium import webdriver
import re
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

def detect():
    buchang = 10
    for url in urls:
        print url
        driver.get(url)
        time.sleep(1)
        abiaoqians = driver.find_elements_by_tag_name("a")
        for abiaoqian in abiaoqians:
            content_abiaoqian = abiaoqian.get_attribute("outerHTML")
            if "sogou.com" in  content_abiaoqian:
                print "**"*10
                print content_abiaoqian

detect()