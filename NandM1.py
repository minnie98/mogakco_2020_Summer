N, M = map(int, input().split())
visited = [False for i in range(N)]
out = []
#DFS algorithm
def N_M(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out))) #output
        return
    for i in range(N):
        if not visited[i]: #Explore for Unvisited Nodes
            visited[i] = True #Check visits
            out.append(i+1) #Visit Content
            N_M(depth + 1, N, M) #Recursive
            visited[i] = False #Visit Completed
            out.pop()

N_M(0, N, M)
