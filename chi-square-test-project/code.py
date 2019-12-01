# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data=pd.read_csv(path)

data_sample=data.sample(n=sample_size, random_state=0)

sample_mean=np.mean(data_sample['installment'])
sample_std=round(data_sample['installment'].std(),3)

margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))

lower_limit=round(sample_mean - margin_of_error,2)
upper_limit=round(sample_mean + margin_of_error,2)

confidence_interval = (lower_limit,
                       upper_limit)  

true_mean=np.mean(data['installment'])

inrange="No"

if( true_mean> confidence_interval[0] and true_mean< confidence_interval[1]  ):
    inrange="Yes"

print("True mean ", true_mean)
print("sample std ",sample_std)
print("Lower interval  ", confidence_interval[0])
print("Upper interval  ", confidence_interval[1])
print("inrange ",inrange)




# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

fig, axes = plt.subplots(nrows=3,ncols=1)

#Code starts here
for i in range(len(sample_size)):
    m=[]
    for j in range(10):
        ds_sample=data['installment'].sample(n=sample_size[i])
        ds_sample_mean=(round(np.mean(ds_sample),3))
        m.append(ds_sample_mean)
    mean_series=pd.Series(m)
    axes[i].hist(mean_series)

print(mean_series)


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['new.int.rate']=data['int.rate'].str.slice_replace(-1, repl='')
data['new.int.rate']=data['new.int.rate'].astype(float)
data['new.int.rate']=data['new.int.rate']/100

data['int.rate']=data['new.int.rate']
#print(data.head(5))

z_statistic ,p_value = ztest(data[data['purpose']=='small_business']['int.rate'], value=data['int.rate'].mean(),alternative='larger')
print(float(p_value))
if p_value<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic ,p_value = ztest(data[data['paid.back.loan']=='No']['installment'],data[data['paid.back.loan']=='Yes']['installment'] )
print(float(p_value))
if p_value<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")



# --------------
#Importing header files
import pandas as pd
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here

yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()
#print("YES : \n",yes)
#print("NO : \n",no)

observed=pd.concat([yes.transpose(),no.transpose()],axis=1,keys=['Yes','No'])
print(observed)

chi2, p, dof, ex = chi2_contingency(observed, correction=False)
print("chi2 is :",chi2)

if chi2>critical_value:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")






