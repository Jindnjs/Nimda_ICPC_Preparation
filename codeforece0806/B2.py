import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
results = []

for _ in range(T):
    a1, a2, b1, b2 = map(int, input().split())
    suneet= 0

    cases = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for a_first, b_first, a_second, b_second in cases:
        suneet_wins = 0
        bwins = 0
        if a_first > b_first:
            suneet_wins += 1
        if a_second > b_second:
            suneet_wins += 1
        if a_first == b_first:
            bwins +=1
        if a_second == b_second:
            bwins +=1
        if suneet_wins >= 1:
            if suneet_wins == 2:
                suneet += 1
            else:
                if suneet_wins == 1 & bwins ==1:
                    suneet += 1
                    
    results.append(suneet)

for result in results:
    print(result)