import pandas as pd

#f=open('example_day4.txt')
f=open('input_day4.txt')
#print(f.readlines())

txt=[]
for l in f.readlines():
    line=[]
    for c in range(len(l)-1):
        line.append(l[c])
    txt.append(line)

f.close()

inp=pd.DataFrame(txt)
print(inp)


def test_h(row,col,sign):
    flag=None
    if inp.iloc[row,col+1*sign]=='M':
        if inp.iloc[row,col+2*sign]=='A':
            if inp.iloc[row,col+3*sign]=='S':
                flag=True
    return flag

def test_v(row,col,sign):
    flag=None
    if inp.iloc[row+1*sign,col]=='M':
        if inp.iloc[row+2*sign,col]=='A':
            if inp.iloc[row+3*sign,col]=='S':
                flag=True
    return flag

def test_d(row,col,sign):
    flag=None
    #print(inp.iloc[row+3*sign,col+3*sign])
    if inp.iloc[row+1*sign,col+1*sign]=='M':
        if inp.iloc[row+2*sign,col+2*sign]=='A':
            if inp.iloc[row+3*sign,col+3*sign]=='S':
                flag=True
    return flag

def test_d_mix(row,col,sign1,sign2):
    flag=None
    if inp.iloc[row+1*sign1,col+1*sign2]=='M':
        if inp.iloc[row+2*sign1,col+2*sign2]=='A':
            if inp.iloc[row+3*sign1,col+3*sign2]=='S':
                flag=True
    return flag


count=0
### find all X:
for row in range(inp.shape[0]):#range(4,5): #range(inp.shape[0]):
    #print('row number %d' %row)
    x_list=inp[inp.iloc[row,:]=='X'].index.tolist() ## indeces of x occurrances
    for col in x_list:
        #print('occurance %d' %col)
        if (col+3)<=inp.shape[1]-1: #test horizontal (positive direction)
            #print('passed on horizontal + ')
            if test_h(row,col,sign=1)==True:
                count=count+1
                #print('found xmas')
        if (col-3)>=0: 
            #print('passed on horizontal - ')
            if test_h(row,col,sign=-1)==True:
                count=count+1
                #print('found xmas')
        if (row+3)<=inp.shape[0]-1: #test vertical (positive direction)
            #print('passed on vertical +')
            if test_v(row,col,sign=1)==True:
                count=count+1
                #print('found xmas')
        if (row-3)>= 0: #test vertical (negative direction)
            #print('passed on vertical -')
            if test_v(row,col,sign=-1)==True:
                count=count+1
                #print('found xmas')
        if (col+3) <= inp.shape[1]-1 and (row+3) <= inp.shape[0]-1: #test diagonal + +
            #print(col,row)
            #print('diagonal + +')
            if test_d(row,col,sign=1)==True:
                count=count+1
                #print('found xmas')
        if (col+3) <= inp.shape[1]-1 and (row-3) >= 0: #test diagonal + -
            #print('diagonal +')
            if test_d_mix(row,col,sign1=-1,sign2=1)==True:
                count=count+1
                #print('found xmas')
        if (col-3) >= 0 and (row-3) >=0: # test diagonal --
            #print('diagonal - -')
            if test_d(row,col,sign=-1)==True:
                count=count+1   
                #print('found xmas')
        if (col-3) >= 0 and (row+3) <= inp.shape[0]-1: # test diagonal -+
            #print('diagonal - -')
            if test_d_mix(row,col,sign1=1,sign2=-1)==True:
                count=count+1   
                #print('found xmas') 
    #print(count)    

#print(count)

#### Part 2 #####
def test_x(row,col,sign1,sign2):
    flag=None
    if inp.iloc[row+sign1,col+sign2]=='M':
        if inp.iloc[row-sign1,col-sign2]=='S':
            if inp.iloc[row-sign1,col+sign2]=='M':
                if inp.iloc[row+sign1,col-sign2]=='S':
                    flag=True
            elif inp.iloc[row+sign1,col-sign2]=='M':
                if inp.iloc[row-sign1,col+sign2]=='S':
                    flag=True
    return flag
    



count=0
for row in range(1,inp.shape[0]-1):#range(4,5): #range(inp.shape[0]):
    #print('row number %d' %row)
    a_list=inp[inp.iloc[row,:]=='A'].index.tolist() ## indeces of a occurrances
    for col in a_list:
        #print('occurance %d' %col)
        #if (col+1) <= inp.shape[1]-1 and (col-1) >=0 and (row+1) <= inp.shape[0]-1 and (row-1) >=0: #test diagonal + +
        if (col+1) <= inp.shape[1]-1 and (col-1) >= 0:
            #print(col,row)
            #print('diagonal + +')
            for i in [-1,1]:
                for j in [-1,1]:
                    #print(i,j)
                    if test_x(row,col,sign1=i,sign2=j)==True:
                        #print(row,col)
                        #print(i,j)
                        count=count+1

            
                    
print(count/2)

#print(inp[inp.loc[:,:]=='X'].index.tolist())