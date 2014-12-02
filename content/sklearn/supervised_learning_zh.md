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
    * 1.1.15. Polynomial regression: extending linear models with basis functions
* 1.2. Support Vector Machines
    * 1.2.1. Classification
        * 1.2.1.1. Multi-class classification
        * 1.2.1.2. Scores and probabilities
        * 1.2.1.3. Unbalanced problems
    * 1.2.2. Regression
    * 1.2.3. Density estimation, novelty detection
    * 1.2.4. Complexity
    * 1.2.5. Tips on Practical Use
    * 1.2.6. Kernel functions
        * 1.2.6.1. Custom Kernels
            * 1.2.6.1.1. Using Python functions as kernels
            * 1.2.6.1.2. Using the Gram matrix
            * 1.2.6.1.3. Parameters of the RBF Kernel
    * 1.2.7. Mathematical formulation
        * 1.2.7.1. SVC
        * 1.2.7.2. NuSVC
    * 1.2.8. Implementation details
* 1.3. Stochastic Gradient Descent
    * 1.3.1. Classification
    * 1.3.2. Regression
    * 1.3.3. Stochastic Gradient Descent for sparse data
    * 1.3.4. Complexity
    * 1.3.5. Tips on Practical Use
    * 1.3.6. Mathematical formulation
        * 1.3.6.1. SGD
    * 1.3.7. Implementation details
* 1.4. Nearest Neighbors
    * 1.4.1. Unsupervised Nearest Neighbors
        * 1.4.1.1. Finding the Nearest Neighbors
        * 1.4.1.2. KDTree and BallTree Classes
    * 1.4.2. Nearest Neighbors Classification
    * 1.4.3. Nearest Neighbors Regression
    * 1.4.4. Nearest Neighbor Algorithms
        * 1.4.4.1. Brute Force
        * 1.4.4.2. K-D Tree
        * 1.4.4.3. Ball Tree
        * 1.4.4.4. Choice of Nearest Neighbors Algorithm
        * 1.4.4.5. Effect of leaf_size
    * 1.4.5. Nearest Centroid Classifier
        * 1.4.5.1. Nearest Shrunken Centroid
* 1.5. Gaussian Processes
    * 1.5.1. Examples
        * 1.5.1.1. An introductory regression example
        * 1.5.1.2. Fitting Noisy Data
    * 1.5.2. Mathematical formulation
        * 1.5.2.1. The initial assumption
        * 1.5.2.2. The best linear unbiased prediction (BLUP)
        * 1.5.2.3. The empirical best linear unbiased predictor (EBLUP)
    * 1.5.3. Correlation Models
    * 1.5.4. Regression Models
    * 1.5.5. Implementation details
* 1.6. Cross decomposition
* 1.7. Naive Bayes
    * 1.7.1. Gaussian Naive Bayes
    * 1.7.2. Multinomial Naive Bayes
    * 1.7.3. Bernoulli Naive Bayes
    * 1.7.4. Out-of-core naive Bayes model fitting
* 1.8. Decision Trees
    * 1.8.1. Classification
    * 1.8.2. Regression
    * 1.8.3. Multi-output problems
    * 1.8.4. Complexity
    * 1.8.5. Tips on practical use
    * 1.8.6. Tree algorithms: ID3, C4.5, C5.0 and CART
    * 1.8.7. Mathematical formulation
        * 1.8.7.1. Classification criteria
        * 1.8.7.2. Regression criteria
* 1.9. Ensemble methods
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
