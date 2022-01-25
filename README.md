# Students-Career-Guidance-Prediction-System
1. Django
We check whether Django is installed and which version by running the following
command in a shell prompt (indicated by the $ prefix):
$ python -m django --version
We move to the desirable directory through cd command and run this following
command:
$ django-admin startproject studentcareers
We then create our theblog and members1 folders using command line:
$ mkdir theblog
$ mkdir members1
In our “theblog” folder we have these files:
● __init__.py
● admin.py

● apps.py
migrations/
● __init__.py
● models.py
● tests.py
● urls.py
● views.py
2. Jupyter notebook
● The Jupyter Notebook App is a server-client application that allows editing and running
notebook documents via a web browser. The Jupyter Notebook App can be executed on a
local desktop requiring no internet access (as described in this document) or can be
installed on a remote server and accessed through the internet.
● In addition to displaying/editing/running notebook documents, the Jupyter Notebook App
has a “Dashboard” (Notebook Dashboard), a “control panel” showing local files and
allowing them to open notebook documents or shutting down their kernels.
● References: Jupyter Notebook App in the project homepage and in the official docs.
3. Scikit libraries
● Scikit-learn (Sklearn) is the most useful and robust library for machine learning in
Python. It provides a selection of efficient tools for machine learning and statistical
modeling including classification, regression, clustering and dimensionality reduction via
a consistent interface in Python. This library, which is largely written in Python, is built
upon NumPy, SciPy and Matplotlib.

a. sklearn.model_selection.train_test_split(*arrays, test_size=None,
Table 3.1 scikit library’s train-test split function
train_size=None, random_state=None, shuffle=True, stratify=None)
b. class sklearn.preprocessing.StandardScaler(*, copy=True, with_mean=True,
with_std=True)
Standardize features by removing the mean and scaling to unit variance.
The standard score of a sample x is calculated as:
z = (x - u) / s
where u is the mean of the training samples or zero if with_mean=False, and s is
the standard deviation of the training samples or one if with_std=False.

Centering and scaling happen independently on each feature by computing the
relevant statistics on the samples in the training set. Mean and standard deviation
are then stored to be used on later data using transform.
Standardization of a dataset is a common requirement for many machine learning
estimators: they might behave badly if the individual features do not more or less
look like standard normally distributed data (e.g. Gaussian with 0 mean and unit
variance).
For instance many elements used in the objective function of a learning algorithm
(such as the RBF kernel of Support Vector Machines or the L1 and L2
regularizers of linear models) assume that all features are centered around 0 and
have variance in the same order. If a feature has a variance that is orders of
magnitude larger than others, it might dominate the objective function and make
the estimator unable to learn from other features correctly as expected.
This scaler can also be applied to sparse CSR or CSC matrices by passing
with_mean=False to avoid breaking the sparsity structure of the data.

Table 3.2 scikit library’s standardscaler function
c. class sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, *,
weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski',
metric_params=None, n_jobs=None)

Table 3.3 scikit library’s KNeighboursclassifiers function
