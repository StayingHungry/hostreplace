#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/17 17:31
# @Author  : nanganglei
# @File    : makeFile.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
url = "http://m.sogo.com/web/searchList.jsp?uID=V5npvumGTk-3uIl0&v=5&dp=1&w=1278&t=1508233127824&s_t=1508233130135&s_from=result_up&htprequery=c&keyword="
file = open("query",'r')
file_query = open("wangyeurl",'w')
contents = file.readlines()
for content in contents:
    url_tem = url + content.strip() + "&forceProtocol=http"
    file_query.write(url_tem)
    file_query.write("\n")
file.close()
file_query.close()