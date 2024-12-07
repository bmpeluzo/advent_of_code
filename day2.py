import numpy as np
import pandas as pd

mat=pd.DataFrame([[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[2, 3, 2],
[8, 6, 4, 4, 1],
[1, 3, 6, 7]])

mat=pd.read_csv('input_day2.txt',sep=None,names=np.arange(8))
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

lv_diff=lv_diff.abs()
print(lv_diff)
allowed_step=[1,2,3,float('NaN')]
#print(lv_diff.isin(allowed_step))
lv_allowed=lv_diff.isin(allowed_step)
print(lv_allowed)
#print(lv_diff[lv_diff==True].dropna(ignore_index=True))
lv_allowed=lv_allowed[lv_allowed==True].dropna(ignore_index=True)

print(lv_allowed.shape[0])