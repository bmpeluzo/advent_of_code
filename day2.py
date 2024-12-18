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
#print(lv_diff3.shape)


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
#print(lv_diff3_mix.shape)
#print(lv_diff3_pure.shape)
#print(lv_diff3_zero.shape)


## mixed matrix:
#print(lv_diff3_mix)
test_total=lv_diff3_mix.count(axis=1)             #array containing the number of non NaN elements
test_neg=lv_diff3_mix[lv_diff3_mix<0].count(axis=1) #array containing the number of negative elements in each row
test_pos=lv_diff3_mix[lv_diff3_mix>0].count(axis=1) #array containing the number of positive elements in each row
#print(test_pos)
#print(test_neg)
ind_mix_2=test_total[(test_pos.iloc[:]>=2) & (test_neg.iloc[:]>=2)].index ## levels we will drop because cannot be saved
#print(ind_mix_2)
lv_diff3_mix.drop(ind_mix_2,inplace=True) # drop mixed rows that cannot be saved
#print(lv_diff3_mix)

test_total=lv_diff3_mix.count(axis=1)             #array containing the number of non NaN elements
#test_neg=lv_diff3_mix[lv_diff3_mix<0].count(axis=1) #array containing the number of negative elements in each row
#test_pos=lv_diff3_mix[lv_diff3_mix>0].count(axis=1) #array containing the number of positive elements in each row
test_zero=lv_diff3_mix[lv_diff3_mix==0].count(axis=1)
#ind_mix_3=lv_diff3_mix[(test_zero>0) & (test_neg>0) & (test_pos>0)].index #levels which have mixed and zeroes
ind_mix_3=lv_diff3_mix[(test_zero>0)].index
lv_diff3_mix.drop(ind_mix_3,inplace=True)  ## lv_diff3_mix now has rows that CAN be saved (according to the element to be removed)
#print(lv_diff3_mix)
#lv_diff3_mix_2=lv_diff3_mix.abs()
#n_high=lv_diff3_mix_2[lv_diff3_mix_2>3].count(axis=1)
#lv_diff3_mix.drop(n_high[n_high>0].index,inplace=True)

#print(lv_diff3_mix)
n_pos=lv_diff3_mix[lv_diff3_mix>0].count(axis=1)
n_neg=lv_diff3_mix[lv_diff3_mix<0].count(axis=1)
#print(n_pos)
#print(n_neg)
lv_diff3_mix_neg=lv_diff3_mix.drop(n_pos[n_pos>1].index)
#print(lv_diff3_mix_neg)
n_neg_2=lv_diff3_mix_neg[lv_diff3_mix_neg<-3].count(axis=1) #number of negative elements <-3 in each row
lv_diff3_mix_neg.drop(n_neg_2[n_neg_2>=2].index,inplace=True) #drop rows w/ more than 1 element <-3
print(lv_diff3_mix_neg)
n_elem=lv_diff3_mix_neg.count(axis=1)

#print(lv_diff3_mix_neg)
#print(lv_diff3_mix_pos)
#print(lv_diff3_mix_neg)
#print(n_elem)
#print(lv_diff3_mix_neg.index)

n=0
for i in range(lv_diff3_mix_neg.shape[0]): #lv_diff3_mix_neg.index:
    for j in range(lv_diff3_mix_neg.shape[1]):
        #print(lv_diff3_mix_neg.iloc[i,j])
        if lv_diff3_mix_neg.iloc[i,j]>0:
            if j==0:
                if lv_diff3_mix_neg.iloc[i,:].min() < -3:
                    if lv_diff3_mix_neg.iloc[i,:].min()==lv_diff3_mix_neg.iloc[i,j+1]:
                        if lv_diff3_mix_neg.iloc[i,j+1] + lv_diff3_mix_neg.iloc[i,j] >= -3:
                            n=n+1
                else:
                    print(lv_diff3_mix_neg.iloc[i,:])
                    n=n+1
"""                     
#            if lv_diff3_mix_neg.iloc[i,j] + lv_diff3_mix_neg.iloc[i,j+1]
#            print(lv_diff3_mix_neg.iloc[i,:].min())    #find the lowest element in the row
            #print(lv_diff3_mix_neg.iloc[i,j])
            if j==0 or j==n_elem.iloc[i]-1:
                # test if there's another forbidden element in the row
                #print(lv_diff3_mix_neg.iloc[i,:])
                #if j==0
                ser=lv_diff3_mix_neg.iloc[i,:].drop([j-1,j])
                #print(ser)
#                ser.drop([j-1],inplace=True)
#                print(ser)
                if ser.min() >= -3:
                    if lv_diff3_mix_neg.iloc[i,j]+lv_diff3_mix_neg.iloc[i,j-1] >= -3:
                        print(lv_diff3_mix_neg.iloc[i,:])
            elif lv_diff3_mix_neg.iloc[i,j] + lv_diff3_mix_neg.iloc[i,j-1] >= -3 and lv_diff3_mix_neg.iloc[i,j] + lv_diff3_mix_neg.iloc[i,j-1] != 0:
                # test if there's another forbidden element in the row
                ser=lv_diff3_mix_neg.iloc[i,:].drop([j,j-1])
                if ser.min() >= -3:
                    n=n+1

lv_diff3_mix_pos=lv_diff3_mix.drop(n_neg[n_neg>1].index)
n_elem_pos=lv_diff3_mix_pos.count(axis=1)


for i in range(lv_diff3_mix_pos.shape[0]): #lv_diff3_mix_neg.index:
    for j in range(lv_diff3_mix_pos.shape[1]):
        #print(lv_diff3_mix_neg.iloc[i,j])
        if lv_diff3_mix_pos.iloc[i,j]<0:
            #print(lv_diff3_mix_neg.iloc[i,j])
            if j==0 or j==n_elem_pos.iloc[i]-1:
                # test if there's another forbidden element in the row
                ser=lv_diff3_mix_neg.iloc[i,:].drop([j])
                if ser.max() <= 3:
                    n=n+1
            elif lv_diff3_mix_pos.iloc[i,j] + lv_diff3_mix_pos.iloc[i,j-1] <= 3 and lv_diff3_mix_pos.iloc[i,j] + lv_diff3_mix_pos.iloc[i,j-1] != 0:
                # test if there's another forbidden element in the row
                ser=lv_diff3_mix_neg.iloc[i,:].drop([j,j-1])
                if ser.max() <= 3:
                    n=n+1
"""
## pure matrix:
# get the absolute values to make it easier
#print(lv_diff3_pure)
lv_diff3_pure_2=lv_diff3_pure.abs()
n_high=lv_diff3_pure_2[lv_diff3_pure_2>3].count(axis=1) # the number of bad elements in each row
#print(n_high)
lv_diff3_pure_2.drop(n_high[n_high>1].index,inplace=True)     ## lv_diff3_pure now has rows that CAN be saved (according to the element to be removed)
#print(lv_diff3_pure_2)
n_elem_pure=lv_diff3_pure_2.count(axis=1)
#print(n_elem_pure)
#print(lv_diff3_pure)
#lv_diff3_pure=lv_diff3_pure.abs()
#print(lv_diff3_pure)

n_pure=0
for i in range(lv_diff3_pure_2.shape[0]):
    for j in range(lv_diff3_pure_2.shape[1]):
        if lv_diff3_pure_2.iloc[i,j]>3:
            #print(j,n_elem_pure.iloc[i])
            if j==0 or j==n_elem_pure.iloc[i]-1:
                #print(lv_diff3_pure_2.iloc[i,:])
                n_pure=n_pure+1
            #elif lv_diff3_pure.iloc[i,j-1] + lv_diff3_pure.iloc[i,j+1] <= 3:
                # test if there's another forbidden element in the row
            #    print(lv_diff3_pure.iloc[i,:])
            #    ser=lv_diff3_pure.iloc[i,:].drop([j,j+1])
            #    if ser.min() >= 3:
            #        n_pure=n_pure+1

## zero matrix:
#print(lv_diff3_zero)
n_zero=lv_diff3_zero[lv_diff3_zero==0].count(axis=1) #get the number of zeroes in each col
#print(n_zero)
lv_diff3_zero.drop(n_zero[n_zero>1].index,inplace=True)
#print(lv_diff3_zero)
lv_diff3_zero=lv_diff3_zero.abs()
n_high=lv_diff3_zero[lv_diff3_zero>3].count(axis=1)
#print(n_high)
lv_diff3_zero.drop(n_high[n_high>0].index,inplace=True)
#n_elem_zero=lv_diff3_zero.count(axis=1)
#lv_diff3_zero=lv_diff3_zero.abs()
#print(lv_diff3_zero)

#n_zero=0
n_zero=lv_diff3_zero.shape[0]
"""
for i in range(lv_diff3_zero.shape[0]):
    for j in range(lv_diff3_zero.shape[1]):
        if lv_diff3_zero.iloc[i,j]==0:
            if j==0 or j==n_elem_zero.iloc[i]-1:
                n_zero=n_zero+1
            elif lv_diff3_zero.iloc[i,j-1] + lv_diff3_zero.iloc[i,j+1] <= 3:
                n_zero=n_zero+1
"""
#print(n_zero)

####### final answer #####
print("Number of safe levels - part 2: %d" %(num_allowed+n+n_pure+n_zero))
