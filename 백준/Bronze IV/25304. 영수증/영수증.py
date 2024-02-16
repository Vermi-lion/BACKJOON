#총가격
X = int(input())

#물건 개수
N = int(input())

hap=0

for i in range(0, N, 1) :
    a, b = map(int, input().split())
    hap += (a*b)
    
if hap == X :
    print('Yes')
    
else :
    print('No')