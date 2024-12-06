import numpy as np
import pandas as pd

mat=pd.DataFrame([[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[2, 3, 2, 3, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]])

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
print(lv_diff)
print((lv_diff < 0).all())


#### "2nd derivative: the step of increase or decrease"
df3=lv_diff.iloc[:,:-1]
df4=lv_diff.iloc[:,1:]
df3.columns=np.arange(df3.shape[1])
df4.columns=np.arange(df4.shape[1])
#print(df3)
#print(df4)
step=df4.sub(df3)
print(step)
allowed_step=[-2,-1,0,1,2,float('NaN')]
step2=step.isin(allowed_step)
#print(step2)

print(step2[step2==True].dropna(ignore_index=True))