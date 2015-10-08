#!/usr/bin/env python
# encoding: utf-8


class EndPoint(object):
    """ the api endpoint """
    def __init__(self, name, client, parent=''):
        self.name = name
        self.client = client
        self.parent = parent
        if client.version:
            base_url = '%s/api/%s' % (client.host, client.version)
        else:
            base_url = '%s/api' % (client.host)
        if parent:
            self.endpoint = '%s/%s/%s' % (base_url, parent, name)
        else:
            self.endpoint = '%s/%s' % (base_url, name)

    def __getattr__(self, attr):
        return EndPoint(attr, self.client, self.name)
