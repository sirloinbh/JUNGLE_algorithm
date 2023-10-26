from collections import deque

N=int(input())
graph=[[] for i in range(N)]
for i in range(N):
    a=input()
    for j in range(N):
        graph[i].append(a[j])
        graph[i][j]=int(graph[i][j])
        
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited = [[False]*N for _ in range(N)]
count=[0]

def bfs(a,b,graph,visited,count):

    q=deque([(a,b)])
    visited[a][b]=True
    cnt1=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]!=0:
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    cnt1+=1
                    q.append((nx,ny))
    count.append(cnt1)
    return visited,count

cnt2=0                   
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and visited[i][j]==False:
            bfs(i,j,graph,visited,count)
            cnt2+=1
count[0]=cnt2
count[1:]=sorted(count[1:])
for i in range(len(count)):
   print(count[i]) 