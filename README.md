# Variance-Reduction-Strata--Experimentation

Stratification

Stratified sampling buckets the population into k strata (e.g., countries), and then the experiment random samples individuals from each stratum independently. Let Y_strat be the treatment effect under the stratified sampling and let p_k indicate the proportion of sample size from strata k. The equations below tell us that the treatment effect is the pooled average of the treatment effect in each stratum and is unbiased. The variance is the weighted average of the within-strata variance and effectively removes the between-strata variance. The variance is smaller than the variance under simple random sampling, which includes both the within-strata and the between-strata variance (more info in this paper).

Pros and Cons
The stratification method provides an unbiased estimate of the treatment effect and effectively removes the between-strata variance. However, in practice, it is usually very hard to implement stratified sampling before experiments. However, implementing stratified sampling is complicated and costly in real life. It “requires a queue system and the use of multiple machines.” (Xie & Aurisset, 2016)
“In the online world, because we collect data as they arrive over time, we are usually unable to sample from strata formed ahead of time.” (Deng, Xu, Kohavi, & Walker, 2013)


Post-stratification

In practice, it is a lot more common to do post-stratification than stratification. Post-stratification randomly samples the population first and then places individuals into strata. Similar to stratification, post-stratification can achieve similar variance reduction.
Here is a very simple example where we generate data from four different normal distributions (4 strata), randomly assign individuals to the treatment and control group, add a treatment effect to the treatment group, and visualize the treatment effects via bootstrapping. The treatment effect is calculated as the mean difference between treatment and control without stratification and as the average of the mean difference for each stratum with stratification. From our simple example, we do see a variance reduction with stratification. Crucially, the mean is unchanged, so we should be able to see any experimental effect on the means better now that the variance has been decreased.
