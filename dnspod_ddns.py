#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
__author__ = u'戴喜军'
current_ip = None

# format:  domains = {'sub_domain': record_id}
domains = {
    'test': 35192771,
    'www': 41016542
}


def ddns(sub_domain, record_id, ip):
    para = {
        'login_email': 'you_email@you_email.com',  # 登陆dnspod的账号
        'login_password': 'password',  # 密码
        'domain_id': 2428050,  # 域名ID，使用curl -X POST https://dnsapi.cn/Domain.List -d 'login_email=api@dnspod.com&login_password=password&format=json' 获取
        'record_line': '电信',  # 线路
        'sub_domain': sub_domain,  # 子域名
        'record_id': record_id,  # 子域名ID，使用 curl -X POST https://dnsapi.cn/Record.List -d 'login_email=api@dnspod.com&login_password=password&format=json&domain_id=2317346' 获得
        'value': ip,  # IP
        'format': 'json'  # 返回的格式，默认为XML格式
    }
    data = urllib.urlencode(para)
    req = urllib2.Request('https://dnsapi.cn/Record.Ddns', data)
    req.add_header('Content-type', 'application/x-www-form-urlencoded')
    req.add_header('Accept', 'text/json')
    response = urllib2.urlopen(req)
    return response.read()


def getip():
    req = urllib2.Request('http://www.linuxyunwei.com/ip.php')
    ip = urllib2.urlopen(req).read()
    return ip

if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            if current_ip != ip:
                current_ip = ip
                for k, v in domains.items():
                   print ddns(k, v, ip)
        except Exception, e:
            pass
        time.sleep(300)

