
import math
X, N= int(input()), int(input())
def powersum(x, largerthan):
    if x==0:
        return 1
    return sum(powersum(x-i**N, i) for i in range(largerthan+1, math.ceil(math.pow(x+1,1/N))))

print(powersum(X,0))
