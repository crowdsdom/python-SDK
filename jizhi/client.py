#!/usr/bin/env python
# encoding: utf-8

import requests
import exception


def parse_response(func):
    def new_func(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        try:
            data = res.json()
        except Exception:
            data = None

        if res.status_code != 200 or not data:
            error = data or {'error': res.text}
            raise exception.Error(res.reason, res.status_code, error)

        return data
    return new_func


class Client(object):
    def __init__(self, client_id, client_secret, host='http://account.crowdsdom.com'):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__host = host
        self.access_token = None
        self._token = None

    def get_access_token(self):
        if self.access_token:
            return self.access_token
        return self.fetch_access_token()

    def fetch_access_token(self):
        token_url = "%s/oauth/token" % (self.__host)
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

    @parse_response
    def get(self, url, query=None, headers=None):
        headers = headers or {}
        if self.access_token:
            headers['Authorization'] = self.access_token
        return requests.get(url, params=query, headers=headers)

    @parse_response
    def post(self, url, body=None, files=None, query=None, headers=None):
        headers = headers or {}
        if self.access_token:
            headers['Authorization'] = self.access_token
        return requests.post(url, data=body, files=files, params=query, headers=headers)
