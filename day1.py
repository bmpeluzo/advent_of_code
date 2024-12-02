import numpy as np

#l1=np.array([3,4,2,1,3,3]) #list 1
#l2=np.array([4,3,5,3,9,3]) #list 2

input=np.loadtxt('input_day1.txt',dtype=int) #load input data
l1=input[:,0] #list 1
l2=input[:,1] #list 2

### loop over l1 and l2 until there are no elements left
diff=0
for i in range(len(l1)):
    min1=np.min(l1) #lowest element of l1
    min2=np.min(l2) 
    i1=np.where(l1==min1)[0][0] #index where min1 is located
    i2=np.where(l2==min2)[0][0]
    diff=diff+np.abs(min1-min2) #compute the different min1-min2 and collect in diff
    l1=np.delete(l1,i1)
    l2=np.delete(l2,i2)

print(diff)