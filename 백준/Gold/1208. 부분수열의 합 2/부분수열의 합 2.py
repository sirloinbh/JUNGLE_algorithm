from collections import defaultdict

def countSubsequence(start, end, weight, subsequence):
    if start == end:
        subsequence[weight] += 1
        return
    countSubsequence(start+1, end, weight, subsequence)
    countSubsequence(start+1, end, weight+nums[start], subsequence)

N, S = map(int, input().split())
nums = list(map(int, input().split()))

subsequence1, subsequence2 = defaultdict(int), defaultdict(int)
countSubsequence(0, N//2, 0, subsequence1)
countSubsequence(N//2, N, 0, subsequence2)

subsequence2_keys = list(subsequence2.keys())
subsequence2_keys.sort()
result = 0

for key in subsequence1.keys():
    target = S - key
    start, end = 0, len(subsequence2_keys)
    while start < end:
        mid = (start + end)//2
        if subsequence2_keys[mid] < target:
            start = mid + 1
        else:
            end = mid
    if end < len(subsequence2_keys) and subsequence2_keys[end] == target:
        result += subsequence1[key] * subsequence2[target]

if S == 0: result -= 1
print(result)
