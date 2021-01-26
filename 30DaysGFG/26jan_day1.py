class Solution:
    def prank(self, a, n): 
        #code here
        for i in range(len(n)):
            a[i]+=(a[a[j]]%n)*n
            
        for i in range(n):
            a[i]=a[i]//n

#prewritten
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ob.prank(a, n)
        for i in a:
            print(i,end=" ")
        print()
