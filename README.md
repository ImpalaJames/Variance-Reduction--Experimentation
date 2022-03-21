# Variance-Reduction-Strata--Experimentation

## Stratification

Stratified sampling buckets the population into k strata (e.g., countries), and then the experiment random samples individuals from each stratum independently. Let Y_strat be the treatment effect under the stratified sampling and let p_k indicate the proportion of sample size from strata k. The equations below tell us that the treatment effect is the pooled average of the treatment effect in each stratum and is unbiased. The variance is the weighted average of the within-strata variance and effectively removes the between-strata variance. The variance is smaller than the variance under simple random sampling, which includes both the within-strata and the between-strata variance (more info in this paper).
![alt text](https://github.com/ImpalaJames/Variance-Reduction--Experimentation/blob/main/Strata.png)
![alt text](https://github.com/ImpalaJames/Variance-Reduction--Experimentation/blob/main/Strata%20formula.png)

### Pros and Cons
The stratification method provides an unbiased estimate of the treatment effect and effectively removes the between-strata variance. However, in practice, it is usually very hard to implement stratified sampling before experiments. However, implementing stratified sampling is complicated and costly in real life. It “requires a queue system and the use of multiple machines.” (Xie & Aurisset, 2016)
“In the online world, because we collect data as they arrive over time, we are usually unable to sample from strata formed ahead of time.” (Deng, Xu, Kohavi, & Walker, 2013)


## Post-stratification

In practice, it is a lot more common to do post-stratification than stratification. Post-stratification randomly samples the population first and then places individuals into strata. Similar to stratification, post-stratification can achieve similar variance reduction.
Here is a very simple example where we generate data from four different normal distributions (4 strata), randomly assign individuals to the treatment and control group, add a treatment effect to the treatment group, and visualize the treatment effects via bootstrapping. The treatment effect is calculated as the mean difference between treatment and control without stratification and as the average of the mean difference for each stratum with stratification. From our simple example, we do see a variance reduction with stratification. Crucially, the mean is unchanged, so we should be able to see any experimental effect on the means better now that the variance has been decreased.
![alt text](https://github.com/ImpalaJames/Variance-Reduction--Experimentation/blob/main/Post%20Strata.png)

## CUPED
Controlled-experiment using pre-experiment data was first introduced by Alex Deng, Ya Xu, Ron Kohavi, and Toby Walker from Microsoft in 2013 and has been widely used in big tech companies such as Netflix, bookings.com, TripAdvisor, and many others. CUPED uses pre-experiment data X (e.g., pre-experiment values of Y) as a control covariate.
![alt text](https://github.com/ImpalaJames/Variance-Reduction--Experimentation/blob/main/CUPED%20Formula.png)
In other words, the variance of Y is reduced by (1-Corr(X, Y)). We would need the correlation between X and Y to be high for CUPED to work well. In the original paper, it is recommended to use the pre-experiment value of Y as X.

### Pros and Cons
CUPED is super easy to use and implement. However, the covariate selection can be tricky, especially when the pre-experiment measure of the target variable is not available. The covariate has to be correlated with the target measure, but not related to the experiment. The scenario where there are multiple covariates can be tricky to deal with in practice.


## Variance_Weighted Estimators
First developed by KevinLiou and Sean Taylor from Facebook and Lyft in 2020. The main idea of the method is to give more weight to users who have lower pre-experiment variance. This method relaxed the homoscedastic variance assumption and instead assumes that each individual can have its own metric variance. 
![alt text](https://github.com/ImpalaJames/Variance-Reduction--Experimentation/blob/main/Variance%20Weighted%20Estimators%20Formula.png)

Similar to CUPED, the variance-weighted estimators also use pre-experiment data. However, weighting induced biases. To reduce bias, the paper proposed a method to bucket users based on their pre-experiment variances, calculates the mean of the treatment effect and pre-experience variance within each bucket, and then calculates the weighted treatment effect across strata. So overall in practice, we would estimate the variance, bucket the variance into k strata, weigh each stratum by the inverse variance, and calculate the weighted treatment effect.
