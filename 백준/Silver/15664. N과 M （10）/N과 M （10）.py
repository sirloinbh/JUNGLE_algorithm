N, M = map(int, input().split())  # N과 M의 값을 입력 받음
nums = list(map(int, input().split()))  # 주어진 N개의 수를 리스트로 입력 받음
nums.sort()  # 주어진 N개의 수를 오름차순 정렬

visited = [False] * N  # 각 숫자의 방문 여부를 확인할 리스트
result = []  # 백트래킹으로 만들 수열을 저장할 리스트

def dfs(depth, start):
    # 현재 만들고 있는 수열의 길이가 M과 같아지면 (즉, M개의 수를 모두 선택했을 때)
    if depth == M:
        print(' '.join(map(str, result)))  # 결과 리스트를 공백으로 구분하여 출력
        return

    overlap = 0  # 이전에 사용한 숫자를 저장하여 중복 제거
    for i in range(start, N):
        # i번째 숫자를 아직 선택하지 않았으며, 이전에 사용한 숫자와 다르면
        if not visited[i] and overlap != nums[i]:
            visited[i] = True  # i번째 숫자를 사용했다고 표시
            result.append(nums[i])  # 결과 리스트에 i번째 수를 추가
            dfs(depth + 1, i + 1)  # 다음 수를 선택하기 위해 재귀 호출
            visited[i] = False  # 백트래킹: i번째 숫자의 사용 여부를 초기화
            result.pop()  # 백트래킹: 결과 리스트에서 마지막 원소 제거
            overlap = nums[i]  # 이전에 사용한 숫자 업데이트

dfs(0, 0)  # 백트래킹 시작 (아직 아무 수도 선택되지 않았으므로 depth는 0)