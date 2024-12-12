import numpy as np
import pandas as pd

mat=pd.DataFrame([[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]])

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
lv_diff2=lv_diff.drop(ind_list) #removing mixed and zero rows

lv_diff2=lv_diff2.abs()
#print(lv_diff2)
allowed_step=[1,2,3,float('NaN')]
#print(lv_diff.isin(allowed_step))
lv_allowed=lv_diff2.isin(allowed_step)
#print(lv_allowed)
#print(lv_diff[lv_diff==True].dropna(ignore_index=True))
lv_allowed=lv_allowed[lv_allowed==True].dropna()

num_allowed=lv_allowed.shape[0]
print("Number of safe levels - part 1: %d" %num_allowed)


################ Part 2 ############################
## remove the already safe levels
lv_diff3=lv_diff.drop(lv_allowed.index)
lv_diff3.set_index(np.arange(lv_diff3.shape[0]),inplace=True) #re-indexing the matrix w/ the non-safe levels
#print(lv_diff3)


## split lv_diff3 between matrices containing + and - in the same row; 0; and a matrix containing non-allowed steps
lv_diff3_min=lv_diff3.min(axis=1) #array containing the min element of each row
lv_diff3_max=lv_diff3.max(axis=1) #array containing the max element of each row
lv_diff3_mul=lv_diff3_min.mul(lv_diff3_max) ##array containing min_i * max_i

ind_mix=lv_diff3_mul[lv_diff3_mul<0].index  # get the indices where (min_i * max_i)<0
ind_zero=lv_diff3_mul[lv_diff3_mul==0].index # get the indices where (min_i * max_i)=0
ind_pure=lv_diff3_mul[lv_diff3_mul>0].index # get the indices where (min_i * max_i)>0

lv_diff3_mix=lv_diff3.iloc[ind_mix,:] #submatrix containing mixed arrows
lv_diff3_pure=lv_diff3.iloc[ind_pure,:] #submatrix containing arrows with zeroes
lv_diff3_zero=lv_diff3.iloc[ind_zero,:] #submatrix containing pure arrows


## mixed matrix:
#print(lv_diff3_mix)
test_total=lv_diff3_mix.count(axis=1)             #array containing the number of non NaN elements
test_neg=lv_diff3_mix[lv_diff3_mix<0].count(axis=1) #array containing the number of negative elements in each row
test_pos=lv_diff3_mix[lv_diff3_mix>0].count(axis=1) #array containing the number of positive elements in each row
test_zero=lv_diff3_mix[lv_diff3_mix==0].count(axis=1)
ind_mix_2=test_total[(test_pos.iloc[:]>=2) & (test_neg.iloc[:]>=2)].index ## levels we will drop because cannot be saved
lv_diff3_mix.drop(ind_mix_2,inplace=True) # drop mixed rows that cannot be saved

test_total=lv_diff3_mix.count(axis=1)             #array containing the number of non NaN elements
test_neg=lv_diff3_mix[lv_diff3_mix<0].count(axis=1) #array containing the number of negative elements in each row
test_pos=lv_diff3_mix[lv_diff3_mix>0].count(axis=1) #array containing the number of positive elements in each row
test_zero=lv_diff3_mix[lv_diff3_mix==0].count(axis=1)
ind_mix_3=lv_diff3_mix[(test_zero>0) & (test_neg>0) & (test_pos>0)].index #levels which have mixed and zeroes
lv_diff3_mix.drop(ind_mix_3,inplace=True)  ## lv_diff3_mix now has rows that CAN be saved (according to the element to be removed)
lv_diff3_mix_2=lv_diff3_mix.abs()
n_high=lv_diff3_mix_2[lv_diff3_mix_2>3].count(axis=1)
lv_diff3_mix.drop(n_high[n_high>0].index,inplace=True)


## pure matrix:
# get the absolute values to make it easier
lv_diff3_pure_2=lv_diff3_pure.abs()
n_high=lv_diff3_pure_2[lv_diff3_pure_2>3].count(axis=1) # the number of bad elements in each row
lv_diff3_pure.drop(n_high[n_high>1].index,inplace=True)     ## lv_diff3_pure now has rows that CAN be saved (according to the element to be removed)


## zero matrix:
n_zero=lv_diff3_zero[lv_diff3_zero==0].count(axis=1)
lv_diff3_zero.drop(n_zero[n_zero>1].index,inplace=True)

lv_diff3_zero_2=lv_diff3_zero.abs()
n_high=lv_diff3_zero_2[lv_diff3_zero_2>3].count(axis=1)
lv_diff3_zero.drop(n_high[n_high>0].index,inplace=True)
#print(lv_diff3_zero)


####### clean matrix
print(pd.concat([lv_diff3_mix,lv_diff3_pure,lv_diff3_zero]))