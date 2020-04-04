def checkchar(st):
    p=set(st)
    s={'0','1'}
    if (s==p or p=={'0'} or p=={'1'}):
        return True
    else:
        return False

def check(s, m): 
    l = len(s); 
    c2 = 0; 
    for i in range(0, l - 1):  
        if (s[i] == '1'):
            c2 = c2 + 1
        if ( c2 == m): 
            return True; 
    return False; 
t=int(input(""))
x=1
for test in range(t):
    s=str(input(""))
    y=str()
    n=len(s)
    if(checkchar(s) and n<=100 and n>=1):
        for i in range(len(s)+1):
            if i < len(s):
                if s[i]=='0':
                    if s[i-1]=='1':
                        y+=')'
                    y+=s[i]
                elif s[i]=='1':
                    if s[i-1]=='0' or i==0:
                        y+='('
                    y+=s[i]
                    if i==(n-1):
                        y+=')'
            else:
                break
    print("Case #",x,":",y)
    x+=1
