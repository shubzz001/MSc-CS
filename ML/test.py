N, K = map(int, input().split())
A = input()

max_consecutive = 0
for i in range(N-K+1):
    B = list(A)
    B[i:i+K] = ['1']*K
    consecutive = 0
    curr = 0 
    for j in B:
        if j == '1':
            curr += 1
            consecutive = max(consecutive, curr)
        else:
            curr = 0
    max_consecutive = max(max_consecutive, consecutive)

print(max_consecutive)