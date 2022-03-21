def generate_data(treatment_effect, size):
    # generate y from a normal distribution
    df = pd.DataFrame({'y': np.random.normal(loc=0, scale=1, size=size)})
    # create a covariate that's corrected with y 
    df['x'] = minimize(
        lambda x: 
        abs(0.95 - pearsonr(df.y, x)[0]), 
        np.random.rand(len(df.y))).x
    # random assign rows to two groups 0 and 1 
    df['group'] = np.random.randint(0,2, df.shape[0])
    # for treatment group add a treatment effect 
    df.loc[df["group"] == 1, 'y'] += treatment_effect
    return df    

df = generate_data(treatment_effect=1, size=10000)
theta = df.cov()['x']['y'] / df.cov()['x']['x']
df['y_cuped'] = df.y - theta * df.x

(
    df.hvplot.kde('y', by='group', xlim = [-5,5], color=['#F9a4ba', '#f8e5ad']) 
    + df.hvplot.kde('y_cuped', by='group', xlim = [-5,5], color=['#F9a4ba', '#f8e5ad'])
