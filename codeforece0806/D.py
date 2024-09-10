def is_subsequence(s, t):
    it = iter(s)
    return all(c in it for c in t)

def solve(test_cases):
    results = []
    for s, t in test_cases:
        possible = False
        n = len(s)
        m = len(t)
        
        for i in range(n - m + 1):
            if all(x == '?' or x == y for x, y in zip(s[i:i + m], t)):
                candidate = list(s)
                candidate[i:i + m] = t
                candidate = ''.join(x if x != '?' else 'a' for x in candidate)
                
                if is_subsequence(candidate, t):
                    results.append("YES")
                    results.append(candidate)
                    possible = True
                    break
        
        if not possible:
            results.append("NO")
    
    return results

T = int(input())
test_cases = [input().strip() for _ in range(T*2)]
test_cases = [(test_cases[i], test_cases[i+1]) for i in range(0, len(test_cases), 2)]
results = solve(test_cases)

for result in results:
    print(result)