# K는 이미 가지고 있는 랜선의 개수, N은 필요한 랜선의 개수
K, N = map(int, input().split())
# lan_cables 리스트에 이미 가지고 있는 각 랜선의 길이를 저장
lan_cables = [int(input()) for _ in range(K)]

# 이분 탐색의 시작점으로 가장 짧게 잘랐을 때를, 끝점으로는 랜선 하나의 최대 길이를 설정
start = 1
end = max(lan_cables)

# 이분 탐색 시작
while start <= end:
    # 중간점 계산
    mid = (start + end) // 2
    # 현재 중간점을 랜선의 길이로 잡았을 때, 얻을 수 있는 랜선의 개수를 계산
    total = sum([cable // mid for cable in lan_cables])

    # 만약 해당 길이로 N개 이상의 랜선을 얻을 수 있다면, 랜선의 길이를 늘릴 수 있는 가능성이 있으므로 시작점 변경
    if total >= N:
        start = mid + 1
    # 그렇지 않다면 랜선의 길이를 줄여야 하므로 끝점 변경
    else:
        end = mid - 1

# 이분 탐색이 종료된 후 end 값에는 원하는 랜선의 최대 길이가 저장되어 있음
print(end)