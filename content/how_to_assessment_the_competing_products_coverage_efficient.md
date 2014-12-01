Date: 2014-05-22
Title: 如何高效的评估竞品收录覆盖率
Category: tech
Tag: tech
Slug: how_to_assessment_the_competing_products_coverage_efficient
###前言
>好久没来这里写东西了，作为一个技术人员,还是得写点干货。 也算是对工作中一些难点的感悟吧，有些习惯总得坚持下去才能见到收获。

正式入职百度半年之后因为某些<del>特殊原因</del>，我被transfer到了百度的spider部门。 这个部门就是负责抓取互联网上对百度有意义的资源(此处泛指网页)。

大家都知道，网站是有压力瓶颈的，对于一个站点，不能无限制的抓取。如果`抓取量+用户访问量>网站实际可承受压力`，网站就会出现诸如404等无法正常响应的情况。

而对于整个百度而言，抓取的出口也是有限的,每天抓取的总量就那么多。 所以，如何在有限的资源下尽可能的将有价值的网页抓回来就是一个难题。

评估一个抓取服务质量的好坏，在于这个服务收录整个集合的百分比。

在我接触这个方向时，对于整个服务的质量评估，基本是处于人工加半自动化工具的方式来评估。 而且现成的工具效率也偏低，只能用来做为评估手段，利用产出数据由于数据量太小，没法用于实际的生产环境。

当时我的导师给了我一个任务，就是实现一个自动评估模块，日处理千万量级的url，用以检测百度是否都收录了这些url或者这些url的相同资源。

这个问题的难点在于，怎么判断2个不同的url是否是相同资源。 `相同资源:同一个站点下指向同一个网页的不同url，两者互为相同资源` 简单来说就是2个不同的url，使用浏览器打开后都为同一个实际页面。 对于收录而言，只需要收录了其中一条就算是good case。 所以需要做的事情，就是比较竞品收录的url和内部收录的url两个集合的交集。

###二种解决方案
基于页面内容的相似性检测，比如正文，标题，content等 **1.优点：理论准确性高，长线来看效果好 2.缺点：基础数据要求高，既然已经抓回了网页，就没必要评估是否已经收录。 3.缺点：做的事情和dedup类似，重复造轮子了**

基于url长相的相似性检测。 **1.优点：新东西，之前没人做过类似的。基础数据依赖简单，仅需要url作为原始输入 2.缺点：容易出现技术上难以解决的badcase，遇到这类情况只能靠白名单机制解决**

最后从性价比的角度考虑，选择了第二种相对简单靠谱的方案。

###总体策略
1. 对于每个竞品收录的url，先计算出一个或多个feature，在同一个feature下可以存在不同的资源，但是相同的资源必需存在同一个feature。 feature主要考虑从url的id以及path入手，如 http://bbs.byr.cn/#!article/WorkLife/932151 feature:(WorkLife, 932151) or (932151) 可用的方法有很多，比如提取query部分的最长数字等。 将已经收录的url，通过trie去匹配特征，如果url中存在特征字符串，才会进入到下一轮计算。 通过这种方式，我们可以将需要进行比较的url pair缩小到一个相对可控的范围内。
2. 通过对过滤后的集合进行两两比较，判断竞品url是否存在一个相似url在已收录集合。 这里主要需要比较的是query部分，将query部分相似度最大的那组url认为是相同资源组 当然，还需要剔除一些无效参数的干扰，这里就不细说了。

###效果
第一版的准确和召回均在90%以上，这主要还是依赖于目前dedup策略的效果已经很高，收录部分基本没什么重复和垃圾。 还有就是本身百度收录还是做得很好的，大部分url都能找到相同资源，很特殊的一小部分case也都是一些特殊参数导致的误识别，目前还没发现url长相一致，但指向不同网页的case。所以后继算法上基本不做优化，主要都是通过配置白名单解决。