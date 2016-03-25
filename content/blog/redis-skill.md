Date: 2016-3-25
Title: redis 小技巧
Category: Technology
Tag: tech
Slug: redis-skill

###问题
最近因为米粉节压测,线上会出现不少压测的垃圾数据

不少实例出现了内存暴增的情况

### 解决

一开始使用
<pre><code>redis-cli --bigkeys</code></pre>
扫描大 key,清理了一部分

后来发现这个命令的机制不是全量扫描,只是抽样扫描
<pre><code>--bigkeys          Sample Redis keys looking for big keys.</code></pre>

出于不想背锅的心理,用go写了一个扫描全量key 的小程序.

主要是利用 ***DEBUG OBJECT*** 和 ***scan***这2个命令实现的

逻辑中加了一些条件判断和限速

发现坑真 TM 多啊.4G 大的 key 你能忍?

3个月不访问的数据干嘛不加 ttl.

真心日了狗.

###TIPS

注意 scan 扫描默认只能扫出10个 key

得这么写才能扫出多个 key
<pre><code>
scan 0 MATCH * COUNT 1024
</codeßß></pre>