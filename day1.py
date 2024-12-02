import numpy as np

#l1=np.array([3,4,2,1,3,3])
#l2=np.array([4,3,5,3,9,3])

input=np.loadtxt('input_day1.txt',dtype=int) #load input data
l1=input[:,0] #list 1
l2=input[:,1] #list 2


### loop over l1 and l2 until there are no elements left
diff=0
score=0
l1p=l1 # because we will keepchanging l1 and l2
l2p=l2
for i in range(len(l1)):
    ################ Part 1: get the absolute difference between the two lists ##################
    min1=np.min(l1p) #lowest element of l1
    min2=np.min(l2p) 
    i1=np.where(l1p==min1)[0][0] #index where min1 is located
    i2=np.where(l2p==min2)[0][0]
    diff=diff+np.abs(min1-min2) #compute the different min1-min2 and collect in diff
    l1p=np.delete(l1,i1) ##update l1 and l2 to get the following minima
    l2p=np.delete(l2,i2)
    
    #################### Part 2: get the similarity score #######################
    i21=np.where(l2==l1[i])[0] #index where element i is located in l2
    n=len(i21) #how many times i appears in l2
    score=score+l1[i]*n #compute the similarity score and collect in score


print(diff)
print(score)