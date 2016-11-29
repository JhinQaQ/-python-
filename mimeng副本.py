# -*- coding: utf-8 -*-
import requests
import lxml.html
import sys
import urllib
import urllib2
import os
reload(sys)
sys.setdefaultencoding("utf-8")
foo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=[0,1,2,3,4,5,6,7,8,9]
for s in foo:
    url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;
    for h in fo:
        url2=url1+'%s'%h;
        for i in num:
            url=url2+'%d.html'%i;

            html=requests.get(url).content;
            
            selector=lxml.html.fromstring(html)
            info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
            for each in info:
                print each

# content=selector.xpath('//div[@style="margin: 0px; padding: 0px; box-sizing: border-box !important;"]/text()')
# for text in content:
#     print text


    # for each in info:
    #
    #
    #     listbai.append(each)
    #
    # f=open('white.txt','w')
    # for bai in listbai:
    #
    #     f.write(bai)
    #     f.write('\n')
    #
    # f.close()