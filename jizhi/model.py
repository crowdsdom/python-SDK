#!/usr/bin/env python
# encoding: utf-8


class EndPoint(object):
    """ the api endpoint """
    def __init__(self, name, client, parent=''):
        self.name = name
        self.client = client
        self.parent = parent
        if client.version:
            base_url = '%s/%s' % (client.api_host, client.version)
        else:
            base_url = '%s' % (client.api_host)
        if parent:
            self.endpoint = '%s/%s/%s' % (base_url, parent, name)
        else:
            self.endpoint = '%s/%s' % (base_url, name)

    def __getattr__(self, attr):
        if self.parent:
            parent = '%s/%s' % (self.parent, self.name)
        else:
            parent = self.name
        return EndPoint(attr, self.client, parent)

    def __getitem__(self, name):
        if self.parent:
            parent = '%s/%s' % (self.parent, self.name)
        else:
            parent = self.name
        return EndPoint(name, self.client, parent)
