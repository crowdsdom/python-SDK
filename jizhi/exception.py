#!/usr/bin/env python
# encoding: utf-8


class BaseError(Exception):
    def __init__(self, message, status_code, error_data):
        super(BaseError, self).__init__(message)
        self.status_code = status_code
        self.error_data = error_data


class ApiError(BaseError):
    pass
