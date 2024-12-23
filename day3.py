
#text='xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))' #part1
#text='xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))' #part2
inpt=open('input_day3.txt',encoding='utf-8')

d='mul('
m=0
text=''


for line in inpt:
    text=text+line
inpt.close()

do=True
for e in text.split(d)[1:]:
    s=d
    n=''
    for i in range(4):
        if e[i].isdigit():
            s=s+str(e[i])
            n=n+str(e[i])
        else:
            m1=int(n)
            break
    if e[i]==',':
        s=s+e[i]
        i=i+1
        o=''
        for j in range(i,len(e)):
            if e[j].isdigit():
                #print(e[j])
                s=s+str(e[j])
                o=o+str(e[j])
            else:
                m2=int(o)
                break
        if e[j]==')':
            if do==True:
                s=s+e[j]
                m=m+m1*m2
                print(s)
    ## check for the do/don't
    for k in range(j,len(e)):
        #print(k)
        if e[k:k+2]=='do':
            if e[k+2:k+4]=='()':
                #print(e[k+2:k+4])
                do=True
                k=k+4
            elif e[k+2:k+7]=='n\'t()':
                do=False
                k=k+7
print(m)
            
