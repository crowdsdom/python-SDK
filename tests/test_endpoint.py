#!/usr/bin/env python
# encoding: utf-8

import unittest
from helper import APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, VERSION, BASE_URL
from jizhi import Client, GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH

c = Client(APP_KEY, APP_SECRET, AUTH_HOST, API_HOST, VERSION)
c.set_access_token('token')


class TestEndPoint(unittest.TestCase):
    def test_users(self):
        """
        POST /Users
        """
        Users = c['Users']
        res = POST(Users)
        self.assertEqual(res.request.headers['Authorization'], 'token')
        self.assertEqual(res.request.method, 'POST')
        self.assertEqual(res.request.url, "%s/Users" % (BASE_URL))

    def test_users_me(self):
        """
        GET /Users/me
        """
        Users = c['Users']
        res = GET(Users.me)
        self.assertEqual(res.request.method, 'GET')
        self.assertEqual(res.request.url, "%s/Users/me" % (BASE_URL))

    def test_users_id(self):
        """
        GET /Users/:id
        """
        Users = c['Users']
        res = GET(Users['12345'])
        self.assertEqual(res.request.method, 'GET')
        self.assertEqual(res.request.url, "%s/Users/12345" % (BASE_URL))

    def test_jobTypes(self):
        """
        POST /jobTypes
        """
        jobTypes = c['jobTypes']
        res = POST(jobTypes)
        self.assertEqual(res.request.method, 'POST')
        self.assertEqual(res.request.url, "%s/jobTypes" % (BASE_URL))

    def test_tasks_id_reject(self):
        """
        PUT /Tasks/:id/reject
        """
        Tasks = c['Tasks']
        res = PUT(Tasks['12345'].reject)
        self.assertEqual(res.request.method, 'PUT')
        self.assertEqual(res.request.url, "%s/Tasks/12345/reject" % (BASE_URL))

    def test_tasks_id_approve(self):
        """
        PUT /Tasks/:id/approve
        """
        Tasks = c['Tasks']
        res = PUT(Tasks['12345'].approve)
        self.assertEqual(res.request.method, 'PUT')
        self.assertEqual(res.request.url, "%s/Tasks/12345/approve" % (BASE_URL))

    def test_head_request(self):
        """
        HEAD /Users/id
        """
        Users = c['Users']
        res = HEAD(Users['12345'])
        self.assertEqual(res.request.method, 'HEAD')
        self.assertEqual(res.request.url, "%s/Users/12345" % (BASE_URL))

    def test_delete_request(self):
        """
        DELETE /Users/id
        """
        Users = c['Users']
        res = DELETE(Users['12345'])
        self.assertEqual(res.request.method, 'DELETE')
        self.assertEqual(res.request.url, "%s/Users/12345" % (BASE_URL))

    def test_options_request(self):
        """
        OPTIONS /Users/id
        """
        Users = c['Users']
        res = OPTIONS(Users['12345'])
        self.assertEqual(res.request.method, 'OPTIONS')
        self.assertEqual(res.request.url, "%s/Users/12345" % (BASE_URL))

    def test_patch_request(self):
        """
        PATCH /Users/id
        """
        Users = c['Users']
        res = PATCH(Users['12345'])
        self.assertEqual(res.request.method, 'PATCH')
        self.assertEqual(res.request.url, "%s/Users/12345" % (BASE_URL))

    def test_endpoint(self):
        self.assertEqual(
            c['Users']['12345'].jobs.count.endpoint,
            "%s/Users/12345/jobs/count" % (BASE_URL)
        )
        self.assertEqual(
            c['Users']['12345'].jobs['123'].endpoint,
            "%s/Users/12345/jobs/123" % (BASE_URL)
        )

if __name__ == '__main__':
    unittest.main()
