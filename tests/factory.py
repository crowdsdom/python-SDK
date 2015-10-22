#!/usr/bin/env python
# encoding: utf-8

JOB = {
    "title": u"微博情感分析",
    "description": u"判断博文中所表达的情绪",
    "keywords": ["情感分析", "微博"],
    "questionsType": "internalQuestionsForm",
    "internalQuestionsForm": {
        "questions": [{
            "id": "sentiment",
            "title": u"黄山温泉太啃外地人了一张票298而本地人却58太不合理了！",
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
