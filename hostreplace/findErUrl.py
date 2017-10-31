#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 12:29
# @Author  : nanganglei
# @File    : findErUrl.py

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

my_headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
              'Accept-Encoding' : 'gzip, deflate, br',
              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Referer':'https://wap.sogou.com/web/searchList.jsp?uID=V5npvumGTk-3uIl0&v=5&dp=1&w=1278&t=1508233127824&s_t=1508233130135&s_from=result_up&htprequery=c&keyword=%e5%9c%a3%e5%a2%9f'}

driver = webdriver.PhantomJS(desired_capabilities=dcap)

urls_file = open('wangyeurl', 'r')
urls = urls_file.readlines()
num = len(urls)


def getHost(url):
    proto, rest = urllib.splittype(url)
    res, rest = urllib.splithost(rest)
    print "unkonw" if not res else res


def getUrlFromA():
    erurl= []
    erurl.append("https://wap.sogou.com/web/searchList.jsp")
    erurl.append("https://m.sogou.com/web/searchList.jsp")
    js = []
    js0 = 'var x=document.getElementsByClassName("ad_result");if(x.length>0){for(var i=0;i<x.length;i++)x[i].parentNode.removeChild(x[i])};'#删除广告
    js1 = 'document.getElementById("kmap-right-container").remove()'  #删除相关内容
    js.append(js0)
    js.append(js1)
    index = -1
    for url in urls:
        index = index + 1
        print "****"*10
        driver.get(url.strip())
        for js_code in js:
            try:
                driver.execute_script(js_code)#通过js删除掉页面中的某些元素
            except:
                info = sys.exc_info()
                print info[0],":",info[1]
                continue
        time.sleep(0.2)
        suoyouabiaoqian = driver.find_element_by_class_name("results").find_elements_by_tag_name("a")
        # suoyouabiaoqian = driver.find_elements_by_tag_name("a")
        print "the current url is:" + url.strip()
        print "yigongyou " + str(num) + "  url,zhe shi di " + str(index) + " ge"
        print "a biao qian num is " + str(len(suoyouabiaoqian))
        for abiaoqian in suoyouabiaoqian:
            outterhtml = abiaoqian.get_attribute("outerHTML")
            # 对于已经判断过的元素可以过滤掉
            if "img-tag kmap-img-tag" in outterhtml \
                    or "kmap-person-rel" in outterhtml:
                continue
            try:
                acontent = abiaoqian.get_attribute("href_mock")
                if ".com" not in acontent:
                    # print "mock_xiangduilujing" + getHost(url) + acontent
                    print requests.get(getHost(url) + acontent,headers=my_headers, timeout = 0.5).status_code
                else:
                    # print "mock_jueduilujing" + acontent
                    print requests.get(acontent,headers=my_headers, timeout = 0.5)
            except:
                try:
                    acontent = abiaoqian.get_attribute("href")
                    if ".com" not in acontent:
                        if "/" not in acontent:
                            # print "no url infomation" + abiaoqian.get_attribute("outerHTML")
                            pass
                        else:
                            # print "xiangduilujing" + getHost(url) + acontent
                            url_tiaozhuan = requests.get(getHost(url) + acontent,headers=my_headers, timeout = 0.5).url
                            if "wap.sogou.com" not in url_tiaozhuan and "m.sogou.com" not in url_tiaozhuan:
                                continue
                            else:
                                if "web/searchList.jsp" not in url_tiaozhuan and "app/apkdetail.jsp" not in url_tiaozhuan:
                                    print url_tiaozhuan




                    else:
                        # print "jueduilujing" + acontent
                        try:
                            url_tiaozhuan = requests.get(acontent,headers=my_headers, timeout = 0.5).url
                            if "wap.sogou.com" not in url_tiaozhuan and "m.sogou.com" not in url_tiaozhuan:
                                continue
                            else:
                                if "web/searchList.jsp" not in url_tiaozhuan and "app/apkdetail.jsp" not in url_tiaozhuan:
                                    print url_tiaozhuan

                        except:
                            if "zhihu" in acontent:
                                pass
                except:
                    pass
                    # print "no href and no mock_href" + abiaoqian.get_attribute("outerHTML")
    print erurl


getUrlFromA()
urls_file.close()
driver.quit()