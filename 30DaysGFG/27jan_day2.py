class Solution:
    def findNth(self,N):
        #code here'
        digit=''
        while N!=0:
            digit=str(N%9)+digit
            N=N//9
        return int(digit)
        
t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
