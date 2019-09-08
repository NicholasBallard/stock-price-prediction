#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.today()

df = web.DataReader("BABA", 'yahoo', start, end)
# -- or --
# df = pd.read_csv('./BABA.csv')
df.tail()

