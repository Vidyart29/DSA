#solution

t=int(input())
for _ in range(t):
    Nsetters, Kproblems,Ddays = [int(Nsetters) for Nsetters in input().split()]
    A=list(map(int,input().split()))
    s=0
    for i in A:
        s+=i
    ans=s//Kproblems
    print(ans if ans <=Ddays else Ddays)
