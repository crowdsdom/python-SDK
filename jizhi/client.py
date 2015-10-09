#!/usr/bin/env python
# encoding: utf-8

import requests
import exception
import model


def parse_response(func):
    def new_func(self, *args, **kwargs):
        headers = kwargs.get('headers', None) or {}
        if self.access_token:
            headers['Authorization'] = self.access_token
            kwargs['headers'] = headers
        res = func(self, *args, **kwargs)
        try:
            data = res.json()
        except Exception:
            data = None

        if res.status_code != 200 or not data:
            error = data or {'error': res.text}
            raise exception.ApiError(res.reason, res.status_code, error)

        return data
    return new_func


class Client(object):
    def __init__(self, client_id, client_secret,
                 auth_host='http://account.crowdsdom.com',
                 api_host='https://developer.crowdsdom.com',
                 version=''):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.auth_host = auth_host
        self.api_host = api_host
        self.version = version
        self.access_token = None
        self._token = None

    def get_access_token(self):
        if self.access_token:
            return self.access_token
        return self.fetch_access_token()

    def set_access_token(self, token):
        self.access_token = token
        return token

    def fetch_access_token(self):
        token_url = "%s/oauth/token" % (self.auth_host)
        self._token = self.post(
            token_url,
            {
                'client_id': self.__client_id,
                'client_secret': self.__client_secret,
                'grant_type': 'client_credentials'
            }
        )
        self.access_token = self._token['access_token']['id']
        return self.access_token

    def delete(self, url, query=None, body=None, headers=None, *args, **kwargs):
        return self.request('delete', url, params=query, data=body, headers=headers, *args, **kwargs)

    def get(self, url, query=None, headers=None):
        return self.request('get', url, params=query, headers=headers)

    def head(self, url, query=None, headers=None):
        return self.request('head', url, params=query, headers=headers)

    def post(self, url, body=None, files=None, query=None, headers=None):
        return self.request('post', url, data=body, files=files, params=query, headers=headers)

    def put(self, url, body=None, files=None, query=None, headers=None):
        return self.request('put', url, data=body, files=files, params=query, headers=headers)

    def options(self, url, query=None, *args, **kwargs):
        return self.request('options', url, params=query, *args, **kwargs)

    def patch(self, url, query=None, body=None, *args, **kwargs):
        return self.request('patch', url, params=query, data=body, *args, **kwargs)

    @parse_response
    def request(self, method, url, *args, **kwargs):
        return requests.request(method, url, **kwargs)

    def __getitem__(self, name):
        return model.EndPoint(name, self)


class HTTP(object):
    def __init__(self, method):
        self.method = method

    def __call__(self, resource, *args, **kwargs):
        if not isinstance(resource, model.EndPoint):
            raise TypeError()
        url = resource.endpoint
        method = getattr(resource.client, self.method)
        return method(url, *args, **kwargs)


DELETE = HTTP('delete')
GET = HTTP('get')
HEAD = HTTP('head')
POST = HTTP('post')
PUT = HTTP('put')
OPTIONS = HTTP('options')
PATCH = HTTP('patch')
