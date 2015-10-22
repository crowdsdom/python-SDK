# Crowdsdom Python SDK

[![Build Status](https://travis-ci.org/crowdsdom/python-SDK.svg?branch=master)](https://travis-ci.org/crowdsdom/python-SDK)

This is the Python SDK of [Crowdsdom API](http://developer.crowdsdom.com/)


## Install

`pip install jizhi`


## Usage

```python
import jizhi

c = jizhi.Client(APP_KEY, APP_SECRET)
c.get_access_token()
Jobs = c['Jobs']
job = POST(Jobs, job_settings)
```