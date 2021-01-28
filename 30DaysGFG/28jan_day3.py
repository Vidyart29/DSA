class Solution:
    def smallestpositive(self, array, n): 
        array.sort()
        a=1
        for i in array:
            if i <=a:
                a+=i
            else:
                break
        return a
        
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))
