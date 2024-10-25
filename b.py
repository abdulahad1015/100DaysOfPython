import math

def solve():
    n, k = [int(x) for x in input().split()]
    s=input()
    
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char]==k:
            s=s.replace(char,"",k)

    return s
    
    









# t=int(input())
for i in range(1):
    print(f"{solve()}")
        
        # print(i)
    # n=5
    # list=input().split()[:n]
    # a,b=input().split()
    # print(list)
    # print(a,b)