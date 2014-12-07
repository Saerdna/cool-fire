date: 2014-12-06 10:56
category: skill
tags: tech, python, web
authors: saerdna
slug: how_to_post_array_with_python
title: python中post数组参数

今天在写自动预约抢购的模块时发现的问题

需要向网站post这样的数据<code>{'key':[1,2,3]}</code>

post的结果是<code>key=1&key=2&key=3</code>

大家都知道在python对参数做序列化是urlencode,可是直接urlencode的结果如下

```python
In [1]: import urllib
In [2]: help(urllib.urlencode)
In [3]: post_data = {'key':[1,2,3]}
In [4]: urllib.urlencode(post_data)
Out[4]: 'key=%5B1%2C+2%2C+3%5D'

```
查了下stackoverflow，还是有人遇到同样的问题，解决方案是urlencode时加上一个参数。

```python
In [1]: import urllib
In [2]: help(urllib.urlencode)
In [3]: post_data = {'key':[1,2,3]}
In [4]: urllib.urlencode(post_data, True)
Out[4]: 'key=1&key=2&key=3'

```
