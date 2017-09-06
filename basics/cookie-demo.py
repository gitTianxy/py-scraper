# encoding=utf-8
"""
cookie demo
-------------
"""
import urllib2
import cookielib
import urllib


def print_cookie(cookie):
    for item in cookie:
        print 'name:%s, value:%s' % (item.name, item.value)


def read_cookie(url):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    try:
        response = opener.open(url)
        print_cookie(cookie)
        return response.read()
    except urllib2.HTTPError, e:
        print '***', e


def do_login(url, name, passwd):
    global cookie_file
    cookie = cookielib.MozillaCookieJar(cookie_file)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    params = urllib.urlencode(dict(name=name, passwd=passwd))
    try:
        response = opener.open(url + '?' + params)
        cookie.save(ignore_discard=True, ignore_expires=True)
        return response.read()
    except urllib2.HTTPError, e:
        print e


def do_request(url):
    global cookie_file
    cookie = cookielib.MozillaCookieJar()
    cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    try:
        response = opener.open(req)
        return response.read()
    except urllib2.HTTPError, e:
        print e


def login_and_request(login_url, req_url, name, passwd):
    global cookie_file
    # login
    cookie = cookielib.MozillaCookieJar(cookie_file)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    params = urllib.urlencode(dict(name=name, passwd=passwd))
    opener.open(login_url + '?' + params)
    cookie.save(ignore_discard=True, ignore_expires=True)
    # request
    result = opener.open(req_url)
    print result.read()


cookie_file = 'cookie.txt'
baidu_url = 'http://www.baidu.com'
login_url = 'http://localhost:8088/login'
request_url = 'http://localhost:8088/user/list'
if __name__ == '__main__':
    # read cookie demo
    read_cookie(baidu_url)
    # login
    print do_login(login_url, name='kevin', passwd='1234')
    # request
    print do_request(request_url)
    # login & request
    print login_and_request(login_url, request_url, 'kevin', '1234')
