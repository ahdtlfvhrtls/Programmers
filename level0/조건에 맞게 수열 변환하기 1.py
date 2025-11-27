def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            i /= 2
        elif i < 50 and i % 2 == 1:
            i *= 2
        else:
            i == i
        answer.append(i)
    return answer    

