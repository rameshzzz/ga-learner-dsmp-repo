# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

data_file=path
data=np.genfromtxt(data_file,delimiter=",",skip_header=1)

print("\n Data :\n",data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
b=np.array(new_record)
print(b)

#Code starts here
census=np.concatenate((data,b),axis=0)
print("\n Census :\n",census)


# --------------
#Code starts here
print(census)
age=census[:,0]
print(age)
max_age=np.amax(age)
print(max_age)
min_age=np.amin(age)
print(min_age)
age_mean=np.nanmean(age)
print(age_mean)
age_std=np.nanstd(age)
print(age_std)
#age=np.array[census[0]]
#print(age)


# --------------
#Code starts here
#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here


# --------------
#Code starts here

import numpy as np 

senior_citizens=census[census[:,0]>60]
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

import numpy as np 

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
print(high)
print(len(high))
print(low)
print(len(low))
avg_pay_high=high.mean(axis=0)[7]
print(avg_pay_high)
avg_pay_low=low.mean(axis=0)[7]
print(avg_pay_low)


