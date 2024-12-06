import numpy as np
import pandas as pd

mat=pd.DataFrame([[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[2, 3, 2],
[8, 6, 4, 4, 1],
[1, 3, 6, 7]])

#mat=pd.read_csv('input_day2.txt',sep=None,names=np.arange(8))
#print(mat)
#print(mat.shape[1])
#print(np.arange(mat.shape[1]))

## new dataframes for the DF subtraction ###
df1=mat.iloc[:,:-1]
df2=mat.iloc[:,1:]
df2.columns=np.arange(df2.shape[1])  # relabeling the columns so that the subtraction is "defined"
#print(df1)
#print(df2)
lv_diff=df2.sub(df1)     # this subtraction tells whether two adjacent numbers are increasing or decreasing
#print(lv_diff)

## filter out the mixed rows (containing both negative and positive elements) and rows containing zeros
lv_diff_min=lv_diff.min(axis=1) #array containing the min element of each row
lv_diff_max=lv_diff.max(axis=1) #array containing the max element of each row
lv_diff_mul=lv_diff_min.mul(lv_diff_max)

ind_list=lv_diff_mul[lv_diff_mul<=0].index #collecting indices where we should filter out rows
lv_diff.drop(ind_list,inplace=True) #removing mixed and zero rows

#print(lv_diff)

#### "2nd derivative: the step of increase or decrease"
df3=lv_diff.iloc[:,:-1]
df4=lv_diff.iloc[:,1:]
df3.columns=np.arange(df3.shape[1])
df4.columns=np.arange(df4.shape[1])
#print(df3)
#print(df4)
step=df4.sub(df3)
#print(step)
allowed_step=[-2,-1,0,1,2,float('NaN')]  #Filtering the allowed values for the 2nd deriv. Here NaN accounts for the levels with less than 8 elements
step2=step.isin(allowed_step)
#print(step2)

print(step2[step2==True].dropna(ignore_index=True).shape[0])