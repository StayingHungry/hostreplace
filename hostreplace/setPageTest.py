#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/21 15:38
# @Author  : nanganglei
# @File    : setPageTest.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from selenium import webdriver

import urllib
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import  requests


dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36  Safari/601.1")
dcap["phantomjs.page.settings.userAgent"] = (
    # "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    # "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI MLA-TL10 Build/HUAWEIMLA-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36"
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko)"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.get("http://pagetest.sogou-inc.com")
time.sleep(1)
# print driver.page_source
# driver.find_element_by_name("username").text =
driver.switch_to.frame(1)
driver.find_element_by_name("username").send_keys( "nanganglei")
driver.find_element_by_name("password").send_keys( "nanganglei")
driver.find_element_by_id("login").click()
time.sleep(0.1)
url = "http://pagetest.sogou-inc.com/index.php?m=case&a=sr&q=SogouWirelessVr&mod=%CE%DE%CF%DF%D6%AA%C1%A2%B7%BD-sogo"
driver.get(url)
ids = []
entrys = driver.find_elements_by_name("checkcase[]")
print  len(entrys)
for item in entrys:
    ids.append(item.get_attribute("id"))
print ids
for id in ids:
    url_new = url.replace("a=sr","a=view") + "&caseid=" + str(id)
    driver.get(url_new)
    url_texts = driver.find_elements_by_name("url[]")
    for url_text in url_texts:
        url_text_content = url_text.text
        if  len(url_text_content) > 25:
            if "sogou.com" in url_text_content[:24]:
                 xinlianjie = url_text_content[:24].replace("wap.sogou.com","m.sogo.com") + url_text_content[24:]
                 print xinlianjie
                 url_text.clear()
                 url_text.send_keys(xinlianjie)
            else:
                pass
        elif len(url_text_content) < 4:
            continue
        else:
            xinlianjie =  url_text_content.replace("wap.sogou.com","m.sogo.com")
            url_text.clear()
            url_text.send_keys(xinlianjie)
        # print url_text_content
    # driver.save_screenshot("test1.png")f
    driver.find_element_by_id("submit_btn").click()
    print url_new
# driver.find_element_by_css_selector("#result_content > a").click()
# driver.switch_to.frame(0)
# projectelment = driver.find_element_by_id("project")
# options = projectelment.find_elements_by_tag_name("option")
# for option in options:
#     if option.text == 'SogouWirelessVr':
#         option.click()
#         break
# time.sleep(0.1)
# driver.find_element_by_id("case").click()
# time.sleep(0.1)
# driver.switch_to.default_content()
# time.sleep(1)
# driver.switch_to.frame("left")
# abiaoqians = driver.find_elements_by_tag_name("a")
# for abiaoqian in abiaoqians:
#     try:
#         if abiaoqian.get_attribute("titel") == "移动版-无线vr是否展现检查_地域类VR-sogo":
#             abiaoqian.click()
#     except:
#         pass
time.sleep(1)
driver.save_screenshot("pagetest.png")
driver.quit()