#!/usr/bin/env python
# encoding: utf-8

import os
import sys
sys.path.append(os.path.realpath(__file__ + '/../..'))
from jizhi import POST, Client
from constants import APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, API_VERSION


c = Client(APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, API_VERSION)

# 相关 api 参考： http://developer.crowdsdom.com/
# 1. 身份验证，获取 access_token
access_token = c.get_access_token()
print('access_token: %s' % access_token)

# 2. 发布任务
# POST /Jobs
Jobs = c['Jobs']
job_settings = {
    "title": "微博情感分析",
    "description": "判断博文中所表达的情绪",
    "keywords": ["情感分析", "微博"],
    "questionsType": "internalQuestionsForm",
    "internalQuestionsForm": {
        "questions": [{
            "id": "sentiment",
            "title": "黄山温泉太啃外地人了一张票298而本地人却58太不合理了！",
            "isRequired": True,
            "answerType": "selectionAnswer",
            "selectionAnswerSpec": {
                "minSelectionCount": 1,
                "maxSelectionCount": 1,
                "style": "radiobutton",
                "optionSpecs": [
                    {"id": "positive", "text": "正面"},
                    {"id": "negative", "text": "负面"},
                    {"id": "neutral", "text": "中性"}
                ]
            }
        }]
    },
    "reward": {"amount": 0.1, "currencyCode": "CNY"}
}
job = POST(Jobs, job_settings)
print('job:', job)
