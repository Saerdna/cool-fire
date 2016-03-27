Date: 2016-3-27
Title: golang map interface to struct
Category: Technology
Tag: tech, golang
Slug: golang-mapinterface-to-struct

最近在弄一个参数检查的功能,需要根据外部的数据来对请求 api 的参数进行检查
>其实就是为了减少别人乱传参数害我来背锅

外部的数据是一个大 <code>JSON</code>,还是多层嵌套那种.

类似这种
<pre>
<code>
{
    "body": {
        "key": {
            "string": "value",
            "int_array": [1,2,3],
            "map": {
                "key": "value"
            }
        }
    }
}
</code>
</pre>

开始的时候把问题想简单了,直接用<code>encoding/json</code>硬来

大家都知道,硬上一般是不太好的嘛.错误的姿势就不给大家示范了,最好不要学我.

主要的问题在于 golang 对于结构体的转换是没法直接转的,需要自己利用反射来扫描map 的每个一 item.

还有一个坑就是 golang 的 json 对于 float 和 int 的处理有些问题,明明是 int,可是拿到手就变成了 float.

这个坑卡了我半个晚上,日了🐶

### 解决方案

其实你既然看到这里一定是想要一个解决方案,我不给肯定是不行的了.

解决方案就在这里 [https://github.com/mitchellh/mapstructure](https://github.com/mitchellh/mapstructure)

还是国外大神给力,在我看到这个模块几百行的代码之后我觉得不再自己造轮子了,而且基本上各种乱七八糟的类型都支持,基本不会有什么大坑,可以放心拿来食用.
