#!/usr/bin/env python
# encoding: utf-8

import os
import sys
sys.path.append(os.path.realpath(__file__ + '/../..'))
import requests
from jizhi import Client

APP_KEY = 'your client app key'
APP_SECRET = 'your client app secret'
AUTH_HOST = 'https://account.crowdsdom.com'
API_HOST = 'https://api.crowdsdom.com'
VERSION = 'v1'
BASE_URL = '%s/%s/api' % (API_HOST, VERSION)


class MockHTTPAdapter(requests.adapters.BaseAdapter):
    def close(self):
        """ do nothing """

    def send(self, request, stream=False, timeout=None,
             verify=True, cert=None, proxies=None):
        res = requests.Response()
        res.request = request
        return res


def mock_request(self, method, url, *args, **kwargs):
    headers = kwargs.get('headers', None) or {}
    if self.access_token:
        headers['Authorization'] = self.access_token
        kwargs['headers'] = headers

    session = requests.Session()
    session.mount('https://', MockHTTPAdapter())
    session.mount('http://', MockHTTPAdapter())
    response = session.request(method=method, url=url, **kwargs)
    session.close()
    return response


origin_request = Client.request
Client.request = mock_request
