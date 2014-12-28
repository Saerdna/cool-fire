date: 2014-12-06 02:56
category: skill
tags: tech, python, mac, web
authors: saerdna
slug: install_pyv8_in_mac
title: 在mac下安装pyv8


### 需求起因
最近在写一个自动登录网站并执行某些操作的模块。

网站在js中加了token，需要在登录的时候传过去做校验。

<pre><code>var JSP_VAR={
  callback:"callbackurl",
  sid:"sid",
  qs:"qs_string",
  hidden:"",
  "_sign":"token",
};
</code></pre>
### 尝试解决

开始尝试直接正则抠出字符串后<code>json.loads</code>，发现和标准json不大一致，遂作罢。

后来发现还有pyv8这种神奇的货色，考虑到以后需求肯定不单单是提取js的数据，也会有一些执行的东西，就想着试试。

执行<code>pip install pyv8</code>后提示
> src/Exception.h:6:16: fatal error: v8.h: no such file or directory

参考了这个哥们的文章之后发现还是不行，安装v8后没有出现boost部分的错误。building PyV8的时候报错了，[错误日志]({filename}/files/pyv8_install_failed.log)。

### 解决方案

无奈之下只好找了个[PyV8-OS-X](https://github.com/brokenseal/PyV8-OS-X)直接拿来用，缺点是以后移植到linux平台下还得改代码。

##### mac版：
<pre><code>from pyv8 import PyV8
</code></pre>
##### linux版：
<pre><code>import PyV8
</code></pre>

为了这个事情都折腾半天了，实在不划算，对于一个程序员来说，折腾这种环境的事情实在太浪费时间了,下次一定得搞一台mini主机，开发运维啥的都统一到ubuntu，就不会有这些破事了。
