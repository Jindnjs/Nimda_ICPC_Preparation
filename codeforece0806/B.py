import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    inp = list(map(int, input().split()))
    

    rou = 0

    sujin = 0
    if inp[0] > inp[2]:
        sujin += 1
    if inp[1] > inp[3]:
        sujin +=1
    
    if sujin >= 2:
        rou +=1

    sujin = 0    
    if inp[0] > inp[3]:
        sujin += 1
    if inp[1] > inp[2]:
        sujin +=1
    if sujin >= 2:
        rou +=1
        
    sujin = 0
    if inp[1] > inp[3]:
        sujin += 1
    if inp[0] > inp[2]:
        sujin +=1
    
    if sujin >= 2:
        rou +=1

    sujin = 0
    if inp[1] > inp[2]:
        sujin += 1
    if inp[0] > inp[3]:
        sujin +=1
    
    if sujin >= 2:
        rou +=1

    print(rou) 