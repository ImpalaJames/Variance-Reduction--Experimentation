import pandas as pd
import numpy as np
import hvplot.pandas
from scipy.stats import pearsonr
from scipy.optimize import minimize

def generate_strata_data(treatment_effect, size):
    # for each strata, generate y from a normal distribution
    df1 = pd.DataFrame({'strata': 1, 'y': np.random.normal(loc=10, scale=1, size=size)})
    df2 = pd.DataFrame({'strata': 2, 'y': np.random.normal(loc=15, scale=2, size=size)})
    df3 = pd.DataFrame({'strata': 3, 'y': np.random.normal(loc=20, scale=3, size=size)})
    df4 = pd.DataFrame({'strata': 4, 'y': np.random.normal(loc=25, scale=4, size=size)})
    df = pd.concat([df1, df2, df3, df4])
    # random assign rows to two groups 0 and 1 
    df['group'] = np.random.randint(0,2, df.shape[0])
    # for treatment group add a treatment effect 
    df.loc[df["group"] == 1, 'y'] += treatment_effect
    return df   

def meandiff(df):
    return df[df.group==1].y.mean() - df[df.group==0].y.mean()

def strata_meandiff(df):
    get_sum = 0
    for i in df.strata.unique():
        get_sum += meandiff(df[df.strata==i])
    return get_sum/len(df.strata.unique())


meandiff_lst = []
strata_meandiff_lst = []
for i in range(100):
    df = generate_strata_data(treatment_effect=1, size=100)
    meandiff_lst.append(meandiff(df))
    strata_meandiff_lst.append(strata_meandiff(df))
    
(
    pd.DataFrame(strata_meandiff_lst).hvplot.kde(label='Stratification') 
    * pd.DataFrame(meandiff_lst).hvplot.kde(label='Original')
)
