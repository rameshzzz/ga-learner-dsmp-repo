# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts 
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include ='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include ='number')
print(numerical_var)





# code ends here


# --------------
# code starts here

banks=bank.drop(['Loan_ID'], axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
print("---------")
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount', aggfunc=np.mean)

print(avg_loan_amount)


# code ends here



# --------------
# code starts here
loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse=len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
print(loan_approved_se)
print(loan_approved_nse)
Loan_Status=614
percentage_se=(loan_approved_se/Loan_Status)*100
percentage_nse=(loan_approved_nse/Loan_Status)*100



# code ends here


# --------------
# code starts here

def months_to_year(months):
    return months/12

banks['loan_term'] = banks['Loan_Amount_Term'].apply(months_to_year)

loan_term=banks.apply(lambda x: months_to_year(x['Loan_Amount_Term']),axis=1)
print(loan_term)

big_loan_term=len(loan_term[loan_term>=25].index)
print(big_loan_term)
# code ends here


# --------------
# code starts here


loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
mean_values=loan_groupby.mean()

# code ends here


