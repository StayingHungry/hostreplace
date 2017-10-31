#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 12:28
# @Author  : nanganglei
# @File    : test_requests.py
# a very short timeout is set intentionally
import requests

# cs_url = 'http://m.sogou.com/web/uID=V5npvumGTk-3uIl0/v=5/type=1/sp=1/ct=171018133555/keyword=%E5%9C%A3%E5%A2%9F/id=614d2b34-4623-4a15-9f12-c2aaa233232f/sec=UuVOZqpeKGsKXIQZX3cYJA../dp=1/vr=11000306/k=%E5%9C%A3%E5%A2%9F/tc?userGroupId=19&dp=1&key=%E5%9C%A3%E5%A2%9F&pno=1&g_ut=3&is_per=0&clk=1&url=http%3A%2F%2Fk.sogou.com%2Fvrtc%2Fdetail%3Fmd%3D814832487473755376%26id%3D4728790430909805736%26cmd%3D814832487473741824%26url%3Dhttp%253A%252F%252Fwww.31xs.com%252F1%252F1886%252F4192618.html%26gf%3Devryw-d-p-i&vrid=11000306&wml=1&linkid=begin&nd=1'
# cs_url = "http://m.sogou.com/web/uID=V5npvumGTk-3uIl0/v=5/type=1/sp=1/ct=171018133433/keyword=%E5%9C%A3%E5%A2%9F/id=722d6ae8-bd31-4805-887e-127734aba34c/sec=kvKGBobKaBnYl2PQi6423w../dp=1/vr=11009501/tc?userGroupId=4&dp=1&key=%E5%9C%A3%E5%A2%9F&pno=1&g_ut=3&is_per=0&pg=webz&clk=10&url=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F52151627%23answer-50026742&f=0&vrid=11009501&linkid=0&wml=1&w=1281"
cs_url = "https://m.sogou.com/web/uID=V5npvumGTk-3uIl0/v=5/type=1/sp=1/ct=171018133433/keyword=%E5%9C%A3%E5%A2%9F/id=722d6ae8-bd31-4805-887e-127734aba34c/sec=kvKGBobKaBnYl2PQi6423w../dp=1/vr=11003501/tc?userGroupId=4&dp=1&key=%E5%9C%A3%E5%A2%9F&pno=1&g_ut=3&is_per=0&&wml=1&clk=11&vrid=11003501&abtestid=3&k_uuid=722d6ae8-bd31-4805-887e-127734aba34c&multi=1&dimension=%E7%9B%B8%E5%85%B3%E6%96%87%E5%AD%A6%E4%BD%9C%E5%93%81&url=https%3A%2F%2Fwap.sogou.com%2Fweb%2FsearchList.jsp%3Fs_from%3Dkmap_recommend%26pid%3Dsogouwap%26dp%3D1%26keyword%3D%25E4%25B8%2580%25E5%25BF%25B5%25E6%25B0%25B8%25E6%2581%2592&linkid=0&name=%E4%B8%80%E5%BF%B5%E6%B0%B8%E6%81%92"
cs_url = "http://english.sogou.com/uID=V5npvumGTk-3uIl0/v=5/type=1/sp=1/ct=171018142743/keyword=china/id=8e9a23f7-2a86-4b5f-8ba9-6fc5af8977b7/sec=Fp5-5zdiqE7nozwxssvVuQ../tc?pg=webz&clk=8&url=http%3A%2F%2Fwww.chinahighlights.com%2F&f=0&id=8e9a23f7-2a86-4b5f-8ba9-6fc5af8977b7&key=china&pno=1&g_ut=3&is_per=0&vstype=english&pagetype=result&channel=result_wap&wml=1&w=1281"
my_headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
              'Accept-Encoding' : 'gzip, deflate, br',
              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Referer':'https://english.sogou.com/web/searchList.jsp?uID=V5npvumGTk-3uIl0&v=5&dp=1&w=1278&t=1508233127824&s_t=1508233130135&s_from=result_up&htprequery=c&keyword=%e5%9c%a3%e5%a2%9f'}
r = requests.get(cs_url,headers=my_headers, timeout = 10)
print r.url
print r.status_code
# print r.content