# 입력: 좌표의 개수 N, 좌표 리스트
N = int(input())
coords = list(map(int, input().split()))

# 좌표를 정렬하고, 중복을 제거
sorted_coords = sorted(set(coords))

# 딕셔너리를 이용하여 좌표-압축 값 매핑
coords_dict = {coord: index for index, coord in enumerate(sorted_coords)}

# 원래의 좌표 순서대로 압축 값 출력
print(' '.join(str(coords_dict[coord]) for coord in coords))