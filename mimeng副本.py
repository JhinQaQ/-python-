# -*- coding: utf-8 -*-
import requests
import lxml.html
import sys
import threading
import time
import urllib
import urllib2
import os
reload(sys)
sys.setdefaultencoding("utf-8")
data = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}



def spider1():
    print 'thread1'
    foo=['a','b','c','d','e']
    fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    for s in foo:
        url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;

        for h in fo:
            url2=url1+'%s'%h;

            for i in num:
                url=url2+'%d.html'%i;


                html=requests.get(url,headers=data).content;


                selector=lxml.html.fromstring(html)
                info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
                for each in info:

                    print each

def spider2():
    print 'thread2'
    foo=['f','g','h','i','g']
    fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    for s in foo:
        url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;
        for h in fo:
            url2=url1+'%s'%h;
            for i in num:
                url=url2+'%d.html'%i;

                time.sleep(0.1)


                html=requests.get(url,headers=data).content;

                selector=lxml.html.fromstring(html)
                info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
                for each in info:
                    print each
def spider3():
    print 'thread3'
    foo=['h','i','g','k','l']
    fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    for s in foo:
        url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;
        for h in fo:
            url2=url1+'%s'%h;
            for i in num:
                url=url2+'%d.html'%i;
                time.sleep(0.1)

                print 3

                html=requests.get(url,headers=data).content;

                selector=lxml.html.fromstring(html)
                info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
                for each in info:
                    print each
def spider4():
    print 'thread4'
    foo=['m','n','o','p','q']
    fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    for s in foo:
        url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;
        for h in fo:
            url2=url1+'%s'%h;
            for i in num:
                url=url2+'%d.html'%i;

                html=requests.get(url,headers=data).content;

                selector=lxml.html.fromstring(html)
                info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
                for each in info:
                    print each
def spider5():
    print 'thread5'
    foo=['r','s','t','u','v']
    fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    for s in foo:
        url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;
        for h in fo:
            url2=url1+'%s'%h;
            for i in num:
                url=url2+'%d.html'%i;

                html=requests.get(url,headers=data).content;

                selector=lxml.html.fromstring(html)
                info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
                for each in info:
                    print each
def spider6():
    print 'thread6'
    foo=['w','x','y','z']
    fo=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=[0,1,2,3,4,5,6,7,8,9]
    for s in foo:
        url1='http://blog.sina.com.cn/s/blog_60f286c90102w%s'%s;
        for h in fo:
            url2=url1+'%s'%h;
            for i in num:
                url=url2+'%d.html'%i;

                html=requests.get(url,headers=data).content;

                selector=lxml.html.fromstring(html)
                info=selector.xpath('//div[@class="articalTitle"]/h2/text()')
                for each in info:
                    print each
try:

   threading._start_new_thread(spider1, ())
   threading._start_new_thread(spider2, ())
   threading._start_new_thread(spider3, ())
   threading._start_new_thread(spider4, ())
   threading._start_new_thread(spider5, ())
   threading._start_new_thread(spider6, ())


except:
   print "Error: unable to start thread"

while 1:
   pass

# content=selector.xpath('//div[@style="margin: 0px; padding: 0px; box-sizing: border-box !important;"]/text()')
# for text in content:



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