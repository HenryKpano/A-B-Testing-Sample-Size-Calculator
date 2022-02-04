from statsmodels.stats.power import zt_ind_solve_power
from statsmodels.stats.proportion import proportion_effectsize as es

#define variable for the computation

# current conversion rate or default conversion rate
baseline_conversion = 0.20

# minimum detectable effect - this refes to the sensitivity of the test.
# In other words, it is the smallest relative change in baseline_conversion rate you are interested in detecting
# This is also known as the lift rate between the current conversion rate and the targeted rate
# It is calculated as a percentage of the baseline_conversion
mde = 0.5


alp = 0.05

# alternative hypothesis expected conversion rate
test_group_conversion = baseline_conversion + mde


powerr = 0.8


#ans = zt_ind_solve_power(effect_size=es(prop1=0.20, prop2=0.6), alpha=0.05, power=0.8, alternative="two-sided")

ans = zt_ind_solve_power(effect_size=es(prop1=baseline_conversion, prop2=test_group_conversion), alpha=alp, power=powerr, alternative="two-sided")
print(ans)
