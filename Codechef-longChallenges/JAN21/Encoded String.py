d={"0000":"a","0001":"b","0010":"c","0011":"d","0100":"e","0101":"f","0110":"g","0111":"h","1000":"i","1001":"j",
    "1010":"k","1011":"l","1100":"m","1101":"n","1110":"o","1111":"p"}

for _ in range(int(input())):
    n=int(input())
    s=str(input())
    ans=''

    for x in range(0,n,4):
        # print(d[str(s[x:x+4])],end= '')
        ans+=d.get(s[x:x+4])
    print(ans)
        
        
        
