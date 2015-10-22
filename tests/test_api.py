#!/usr/bin/env python
# encoding: utf-8

import unittest
from helper import (APP_KEY, APP_SECRET, AUTH_HOST, API_HOST,
                    VERSION, ACCESS_TOKEN, USER_ID, mocker)
from factory import JOB
from jizhi import Client, ApiError, GET, POST

c = Client(APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, VERSION)


class TestAPI(unittest.TestCase):
    def setUp(self):
        mocker.start()

    def tearDown(self):
        mocker.stop()

    def test_without_authorizated(self):
        """
        it should return 401 if has not authorizated
        """
        access_token = c.access_token
        c.set_access_token('')
        Users = c['Users']

        with self.assertRaises(ApiError) as cm:
            GET(Users.me)

        self.assertEqual(cm.exception.status_code, 401)

        c.set_access_token(access_token)

    def test_access_token(self):
        access_token = c.get_access_token()
        self.assertEqual(access_token, ACCESS_TOKEN)

    def test_users_me(self):
        Users = c['Users']
        res = GET(Users.me)
        self.assertEqual(res['type'], 'requester')
        self.assertEqual(res['id'], USER_ID)

    def test_jobs(self):
        Jobs = c['Jobs']
        job = POST(Jobs, JOB)
        self.assertEqual(job['title'], JOB['title'])

if __name__ == '__main__':
    unittest.main()
