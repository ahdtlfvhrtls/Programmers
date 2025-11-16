def solution(arr, idx):
    answer = 0
    temp = []
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            temp.append(i)
    if len(temp) == 0:
        answer = -1
    else:
        answer = min(temp)
            
    return answer