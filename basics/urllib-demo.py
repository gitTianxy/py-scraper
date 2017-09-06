# encoding=utf-8
"""
urllib demo
--------------
"""
import urllib
import urllib2
import socket


class Urllib2Demo:
    def __init__(self):
        pass

    def __encode_params(self, params):
        return urllib.urlencode(params)

    def open_url(self, url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        if data:
            data = urllib.urlencode(data)
        response = urllib2.urlopen(url, data, timeout)
        print response.read()

    def open_req(self, url, data=None, method=None, headers={}, proxy=False, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        if data:
            data = self.__encode_params(data)
            if method and method == 'GET':
                url += '?' + data
                data = None
        req = urllib2.Request(url, data, headers)
        if method:
            req.get_method = lambda: method
        if proxy:
            proxy_handler = urllib2.ProxyHandler({
                "http": 'http://localhost:1080',
                "https": 'http://localhost:1080'
            })
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
        resp = urllib2.urlopen(req, timeout=timeout)
        return resp.read()


def test_CRUD():
    """
    user crud
    :return:
    """
    demo = Urllib2Demo()
    test_url = 'http://localhost:8088/'
    path = '/user/list'
    print demo.open_req(test_url + path, method='GET')
    path = '/user'
    print demo.open_req(test_url + path, method='PUT', data={'name': 'kevin', 'age': 18})
    path = '/user/kevin'
    print demo.open_req(test_url + path, method='POST', data={'age': 28})
    path = '/user/kevin'
    print demo.open_req(test_url + path, method='DELETE')


def test_proxy():
    """
    request using proxy
    :return:
    :return:
    """
    demo = Urllib2Demo()
    test_url = 'https://www.google.com/'
    print demo.open_req(test_url, proxy=True)


if __name__ == '__main__':
    demo = Urllib2Demo()
    test_url = 'http://www.baidu.com'
    print demo.open_req(test_url)
