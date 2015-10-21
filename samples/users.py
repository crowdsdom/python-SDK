#!/usr/bin/env python
# encoding: utf-8

import os
import sys
sys.path.append(os.path.realpath(__file__ + '/../..'))
from jizhi import GET, Client
from constants import APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, API_VERSION

c = Client(APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, API_VERSION)

# 相关 api 参考： http://developer.crowdsdom.com/
# 1. 身份验证，获取 access_token
access_token = c.get_access_token()
print('access_token: %s' % access_token)

# 2. 获取用户信息
# GET /Users/me
Users = c['Users']
me = GET(Users.me)
print('me:', me)
