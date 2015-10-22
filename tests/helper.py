#!/usr/bin/env python
# encoding: utf-8

import os
import sys
sys.path.append(os.path.realpath(__file__ + '/../..'))
import requests
import requests_mock
from factory import JOB

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

APP_KEY = 'your client app key'
APP_SECRET = 'your client app secret'
AUTH_HOST = 'https://account.crowdsdom.com'
API_HOST = 'https://api.crowdsdom.com'
ACCESS_TOKEN = 'token'
USER_ID = '561c61802b403114006cdf5d'
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


#################################################################
#                      requests mock                            #
#################################################################
FAKER_DATA = {}


def faker_data_factory(method, path, data):
    path = "%s-/%s/api%s" % (method, VERSION, path)
    FAKER_DATA[path] = data

faker_data_factory(
    'GET', '/users/me',
    {
        'id': USER_ID,
        'type': 'requester'
    }
)
faker_data_factory('POST', '/jobs', JOB)


def auth_host_matcher(request):
    return requests_mock.create_response(
        request,
        json={
            'access_token': {
                'id': ACCESS_TOKEN,
                'ttl': 7200,
                'userId': USER_ID
            },
            'token_type': 'Bearer'
        })


def api_host_matcher(request):
    if (request._request.headers.get('Authorization', None) != ACCESS_TOKEN):
        return requests_mock.create_response(
            request, status_code=401, reason='Unauthorized'
        )
    path = '%s-%s' % (request._request.method, request.path.lower())
    result = FAKER_DATA.get(path, None)
    if not result:
        return requests_mock.create_response(
            request, status_code=404, reason='Not Found'
        )
    return requests_mock.create_response(request, json=result)


def adapter_matcher(request):
    host = "%s://%s" % (request.scheme, request.netloc)
    if host == API_HOST:
        return api_host_matcher(request)
    return auth_host_matcher(request)


mocker = requests_mock.Mocker()
mocker._adapter.add_matcher(adapter_matcher)
