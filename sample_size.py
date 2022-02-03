from statsmodels.stats.power import zt_ind_solve_power
from statsmodels.stats.proportion import proportion_effectsize as es

#define variable for the computation

default_conversion = 0.50
alp = 0.05
test_group_conversion = default_conversion + alp
powerr = 0.8


#ans = zt_ind_solve_power(effect_size=es(prop1=0.50, prop2=0.55), alpha=0.05, power=0.8, alternative="two-sided")

ans = zt_ind_solve_power(effect_size=es(prop1=default_conversion, prop2=test_group_conversion), alpha=alp, power=powerr, alternative="two-sided")
print(ans)