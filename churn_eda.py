# Exploratory Data Analysis (EDA) for the customer churn dataset
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt 

# load data
telco_data = pd.read_csv("/Users/tonyzhang/Desktop/customerchurn/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(telco_data.dtypes) 
# there are a lot of object data types, so we need to perform feature engineering to convert them to numerical data types. 

# descriptive statistics on numerical variables
telco_data.describe()


