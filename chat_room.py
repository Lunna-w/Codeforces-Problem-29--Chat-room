s = ''.join(list(input()))
hello = 'hello'
pos=0


for i in s:
        if (i==hello[pos]):
                pos+=1
        if(pos>=len('hello')):
                break

if(pos==len(hello)):
        print('YES')
else:
        print('NO')