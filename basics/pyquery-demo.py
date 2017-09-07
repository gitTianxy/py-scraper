# encoding=utf-8
"""
PyQuery demo
----------------
NOTE:
    PyQuery支持 Ajax 操作，带有 get 和 post 方法，不过不常用，一般我们不会用 PyQuery 来做网络请求，仅仅是用来解析。
"""
from pyquery import PyQuery as pq
import lxml.etree as etree
from pyquery.ajax import PyQuery as PQAjax

text_test = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''


def load_from_file(file):
    return pq(filename=file)


def load_from_url(url, method='get', data=None, headers={}, cookies={}):
    return pq(url, method=method, data=data, headers=headers, cookies=cookies)


def load_from_str(str):
    return pq(etree.fromstring(str))


if __name__ == '__main__':
    # load data
    doc = load_from_file('test.html')
    print load_from_url('https://www.baidu.com')
    print load_from_url('http://localhost:8088/user/list', cookies=dict(name='kevin'))
    print load_from_str(text_test)
    print '-----------------------'
    # elements
    lis = doc('li')
    for li in lis.items():
        print 'class:%s, text:%s' % (li.attr('class'), li.text())
    # add/remove class
    for li in lis.items():
        if '1' in li.attr('class'):
            li.addClass('cls-1')
        elif 'active' in li.attr('class'):
            li.removeClass('active')
    print lis
    # post data -- not recommend
    # print load_from_url('http://localhost:8088/user/kevin', data=dict(age=28, passwd=1234), method='post',
    #                     cookies=dict(name='kevin'))
