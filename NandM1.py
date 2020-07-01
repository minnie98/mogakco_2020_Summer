N, M = map(int, input().split())
visited = [False for i in range(N)]
out = []

def N_M(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            N_M(depth + 1, N, M)
            visited[i] = False
            out.pop()

N_M(0, N, M)