# CF 561 (Div 2) B

k = int(input())

n,m = 0,0
vowels = "aeiou"

for i in range(5,k):
    if k%i==0 and k//i>=5:
        n,m = i,k//i

if n==0 and m==0:
    print(-1)
else:
    if m==5:
        for a in range(m):
            for b in range(n):
                print(vowels[(a+b)%5], end='')

    else:
        for a in range(k):
            print(vowels[a%5], end='')


