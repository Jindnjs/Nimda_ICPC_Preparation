def can_shower(n, s, m, intervals):
    # 첫 작업 전의 빈 시간
    if intervals[0][0] >= s:
        return "YES"
    
    # 각 작업 사이의 빈 시간 확인
    for i in range(1, n):
        if intervals[i][0] - intervals[i-1][1] >= s:
            return "YES"
    
    # 마지막 작업 후의 빈 시간
    if m - intervals[-1][1] >= s:
        return "YES"
    
    return "NO"

t = int(input())
results = []

for _ in range(t):
    n, s, m = map(int, input().split())
    intervals = []
    for _ in range(n):
        li, ri = map(int, input().split())
        intervals.append((li, ri))
    
    results.append(can_shower(n, s, m, intervals))

for result in results:
    print(result)