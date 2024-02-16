A, B, C = map(int, input().split())

if A == B == C :
    print(10000 + A * 1000) 
    
elif A == B :
    print(1000 + A * 100)
    # 같은 눈을 어떻게 구하느냐
    
elif B == C :
    print(1000 + B * 100)

elif C == A :
    print(1000 + C * 100)
    
    
elif A != B != C :
    max = max(A, B, C)
    print(max * 100)