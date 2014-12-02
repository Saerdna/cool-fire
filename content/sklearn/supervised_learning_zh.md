Date: 2014-12-01
Title: 监督学习
Category: translate
Tag: self-promote, tech
Slug: supervised_learning
lang: zh

###<center>1.监督学习（翻译中）</center>
* 1.1. 广义线性模型
    * 1.1.1. 最小二乘法
        * 1.1.1.1. 最小二乘法复杂度
    * 1.1.2. 岭回归
        * 1.1.2.1. 岭回归复杂度
        * 1.1.2.2. 参数设置:广义交叉验证
    * 1.1.3. 套索算法
        * 1.1.3.1. 参数设置
        	* 1.1.3.1.1. 交叉验证的使用
        	* 1.1.3.1.2. 基于模型选择的信息标准
    * 1.1.4. 弹性网原理
    * 1.1.5. 多任务的套索算法
    * 1.1.6. 最小角回归
    * 1.1.7. 最小角回归 套索
        * 1.1.7.1. 数学公式
    * 1.1.8. 正交匹配追踪算法 (OMP)
    * 1.1.9. 贝叶斯回归
        * 1.1.9.1. 贝叶斯岭回归
        * 1.1.9.2. 自动相关确定 - ARD
    * 1.1.10. 逻辑回归
    * 1.1.11. 随机梯度下降 - SGD
    * 1.1.12. 感知器
    * 1.1.13. 被动侵略算法
    * 1.1.14. 随机抽样一致:增加异常值的鲁棒性
    * 1.1.15. 多项式回归: 基础函数的扩展线性模型
* 1.2. 支持向量机
    * 1.2.1. 分类
        * 1.2.1.1. 多类分类
        * 1.2.1.2. 评分与概率
        * 1.2.1.3. 不平衡问题
    * 1.2.2. 回归
    * 1.2.3. 密度估计,新颖性检测
    * 1.2.4. 复杂度
    * 1.2.5. 实际中使用技巧
    * 1.2.6. 核函数
        * 1.2.6.1. 自定义核
            * 1.2.6.1.1. 用 Python 函数作为核函数
            * 1.2.6.1.2. 使用 Gram 矩阵
            * 1.2.6.1.3. RBF 内核参数
    * 1.2.7. 数学公式
        * 1.2.7.1. SVC
        * 1.2.7.2. NuSVC
    * 1.2.8. 实际细节
* 1.3. 随机梯度下降
    * 1.3.1. 分类
    * 1.3.2. 回归
    * 1.3.3. 稀疏数据的随机梯度下降
    * 1.3.4. 复杂度
    * 1.3.5. 实际中的使用技巧
    * 1.3.6. 数学公式
        * 1.3.6.1. SGD
    * 1.3.7. 实际细节
* 1.4. 最近邻算法
    * 1.4.1. 无监督的近邻算法
        * 1.4.1.1. 找到最近邻
        * 1.4.1.2. KDTree 和 BallTree 类
    * 1.4.2. 最近邻分类问题
    * 1.4.3. 最近邻回归问题
    * 1.4.4. 最近邻算法
        * 1.4.4.1. 暴力
        * 1.4.4.2. K-D Tree
        * 1.4.4.3. Ball Tree
        * 1.4.4.4. 最近邻算法的选择
        * 1.4.4.5. leaf_size 的影响
    * 1.4.5. 最近质心分类
        * 1.4.5.1. 最近的缩小质心
* 1.5. 高斯过程
    * 1.5.1. 例子
        * 1.5.1.1. 一个回归例子的介绍
        * 1.5.1.2. 数据拟合
    * 1.5.2. 数学公式
        * 1.5.2.1. 开始的假设
        * 1.5.2.2. 最佳线性无偏预测 (BLUP)
        * 1.5.2.3. 经验最佳线性无偏预测 (EBLUP)
    * 1.5.3. 相关模型
    * 1.5.4. 回归模型
    * 1.5.5. 实际细节
* 1.6. 交叉分解
* 1.7. 朴素贝叶斯
    * 1.7.1. 高斯朴素贝叶斯
    * 1.7.2. 多项式朴素贝叶斯
    * 1.7.3. 伯努利朴素贝叶斯
    * 1.7.4. 核心朴素贝叶斯模型拟合
* 1.8. 决策树
    * 1.8.1. 分类
    * 1.8.2. 回归
    * 1.8.3. 多输出问题
    * 1.8.4. 复杂度
    * 1.8.5. 实际中的使用技巧
    * 1.8.6. 树算法: ID3, C4.5, C5.0 and CART
    * 1.8.7. 数学公式
        * 1.8.7.1. 分类标准
        * 1.8.7.2. 回归标准
* 1.9. 所有方法
    * 1.9.1. Bagging meta-estimator
    * 1.9.2. Forests of randomized trees
        * 1.9.2.1. Random Forests
        * 1.9.2.2. Extremely Randomized Trees
        * 1.9.2.3. Parameters
        * 1.9.2.4. Parallelization
        * 1.9.2.5. Feature importance evaluation
        * 1.9.2.6. Totally Random Trees Embedding
    * 1.9.3. AdaBoost
        * 1.9.3.1. Usage
    * 1.9.4. Gradient Tree Boosting
        * 1.9.4.1. Classification
        * 1.9.4.2. Regression
        * 1.9.4.3. Fitting additional weak-learners
        * 1.9.4.4. Controlling the tree size
        * 1.9.4.5. Mathematical formulation
            * 1.9.4.5.1. Loss Functions
        * 1.9.4.6. Regularization
            * 1.9.4.6.1. Shrinkage
            * 1.9.4.6.2. Subsampling
        * 1.9.4.7. Interpretation
            * 1.9.4.7.1. Feature importance
            * 1.9.4.7.2. Partial dependence
* 1.10. Multiclass and multilabel algorithms
    * 1.10.1. Multilabel classification format
    * 1.10.2. One-Vs-The-Rest
        * 1.10.2.1. Multiclass learning
        * 1.10.2.2. Multilabel learning
    * 1.10.3. One-Vs-One
        * 1.10.3.1. Multiclass learning
    * 1.10.4. Error-Correcting Output-Codes
        * 1.10.4.1. Multiclass learning
* 1.11. Feature selection
    * 1.11.1. Removing features with low variance
    * 1.11.2. Univariate feature selection
    * 1.11.3. Recursive feature elimination
    * 1.11.4. L1-based feature selection
        * 1.11.4.1. Selecting non-zero coefficients
        * 1.11.4.2. Randomized sparse models
    * 1.11.5. Tree-based feature selection
    * 1.11.6. Feature selection as part of a pipeline
* 1.12. Semi-Supervised
    * 1.12.1. Label Propagation
* 1.13. Linear and quadratic discriminant analysis
    * 1.13.1. Dimensionality reduction using LDA
    * 1.13.2. Mathematical Idea
* 1.14. Isotonic regression
