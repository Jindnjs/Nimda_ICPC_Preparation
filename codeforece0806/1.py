import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for i in range(T):
    inp = input()
    result = int(inp[0]) + int(inp[1])
    print(result)