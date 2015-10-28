.. jizhi documentation master file, created by
   sphinx-quickstart on Wed Oct 28 10:38:14 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

jizhi python-SDK
=================================

安装
^^^^^^^^^^^^^

所需依赖：

* python >= 2.6
* requests >= 2.7.0

使用pip安装::

    pip install jizhi

通过源代码安装::

    git clone https://github.com/crowdsdom/python-SDK
    cd python-SDK
    python setup.py install

快速入门
^^^^^^^^^^^^^

首先获取 AccessToken::

    >>> from jizhi import Client
    >>> c = Client('your client app key', 'your client app secret')
    >>> token = c.get_access_token()

如果之前已经获取过 AccessToken ，也可以直接使用::

    >>> c.set_access_token(token)

然后再根据 http://developer.crowdsdom.com/ 的api文档进行相关操作。
如，发布任务为 ``POST /Jobs`` ，那么对应操作为::

    >>> from jizhi import POST
    >>> Jobs = c['Jobs']
    >>> job = POST(Jobs, body=job_settings)

这里任务发布成功会返回一个 json 格式的数据，如果 api 调用失败则会抛出一个 ``jizhi.ApiError`` 的异常。

因此这里建议进行异常捕获::

    >>> from jizhi import ApiError
    >>> try:
    >>>     job = POST(Jobs, body=job_settings)
    >>> except ApiError as e:
    >>>     print(e.message, e.error_data)

任务发布成功之后，可通过 ``GET /Jobs/:id/tasks`` 查看该任务的结果，对应的操作为::

    >>> from jizhi import GET
    >>> Jobs = c['Jobs']
    >>> tasks = GET(Jobs[job['id']].tasks)

相关说明
------------

jizhi SDK 遵循 RESTful 风格的形式，先通过 client 对象获取到资源对象，然后就可以对该资源对象进行操作。
如, 通过 ``GET /Jobs/{id}/tasks/count`` 接口获取 id 为 ``ab2a03fda3300466356`` 的任务结果数，对应的操作为::

    >>> from jizhi import GET
    >>> Jobs = client['Jobs']
    >>> GET(Jobs.ab2a03fda3300466356.tasks.count)

如果 id 为数字或者是一个变量，则不能使用 ``getattr`` 方式，此时需要使用 ``getitem`` 方式::

    >>> GET(Jobs['1234567'].tasks.count)

或者::

    >>> job_id = '1234567'
    >>> GET(Jobs[job_id].tasks.count)


例子
^^^^^^^^^^^^^

可以通过 https://github.com/crowdsdom/python-SDK/tree/master/samples 获取一些事例，
从而可以快速了解jizhi SDK的使用方法。



.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

