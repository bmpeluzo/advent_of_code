
inpt='xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
inpt=open('input_day3.txt')

d='mul('
m=0
text=''

for line in inpt:
    text=text+line
inpt.close()

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
            s=s+e[j]
            m=m+m1*m2
            print(s)
print(m)
            
