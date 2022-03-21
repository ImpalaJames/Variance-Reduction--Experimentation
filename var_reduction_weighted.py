
def generate_strata_data(treatment_effect, size):
    # for each strata, generate y from a normal distribution
    df1 = pd.DataFrame({'strata': 1, 'pre_experient_variance':1, 'y': np.random.normal(loc=10, scale=1, size=size)})
    df2 = pd.DataFrame({'strata': 2, 'pre_experient_variance':2, 'y': np.random.normal(loc=15, scale=2, size=size)})
    df3 = pd.DataFrame({'strata': 3, 'pre_experient_variance':3, 'y': np.random.normal(loc=20, scale=3, size=size)})
    df4 = pd.DataFrame({'strata': 4, 'pre_experient_variance':4, 'y': np.random.normal(loc=25, scale=4, size=size)})
    df = pd.concat([df1, df2, df3, df4])
    # random assign rows to two groups 0 and 1 
    df['group'] = np.random.randint(0,2, df.shape[0])
    # for treatment group add a treatment effect 
    df.loc[df["group"] == 1, 'y'] += treatment_effect
    return df   

def variance_weighted_meandiff(df):
    weighted_effect_sum = 0
    weights_sum = 0
    for i in df.strata.unique():
        #For each strata, we then calculate its average treatment effect
        treatment_effect_strata = meandiff(df[df.strata==i])
        # estimate its weight based on the inverse within-group estimated variance (such as mean)
        weights_strata = 1/df[df.strata==i]['pre_experient_variance'].mean()
        # calculate the sum of weighted treatment effect
        weighted_effect_sum +=  treatment_effect_strata *  weights_strata
        # calculate the sum of weights
        weights_sum += weights_strata    
    return weighted_effect_sum/weights_sum

def strata_meandiff(df):
    get_sum = 0
    for i in df.strata.unique():
        get_sum += meandiff(df[df.strata==i])
    return get_sum/len(df.strata.unique())


meandiff_lst = []
variance_weighted_meandiff_lst = []
strata_meandiff_lst = []
for i in range(200):
    df = generate_strata_data(treatment_effect=1, size=100)
    meandiff_lst.append(meandiff(df))
    variance_weighted_meandiff_lst.append(variance_weighted_meandiff(df))
    strata_meandiff_lst.append(strata_meandiff(df))
   
(
    pd.DataFrame(variance_weighted_meandiff_lst).hvplot.kde(label='Variance Weighted Estimator')
    * pd.DataFrame(meandiff_lst).hvplot.kde(label='Original')
    * pd.DataFrame(strata_meandiff_lst).hvplot.kde(label='Statification')
)
