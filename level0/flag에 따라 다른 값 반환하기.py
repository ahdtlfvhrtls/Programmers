def solution(a, b, flag):
    answer = 0
    if flag is True:
        answer += (int(a) + int(b))
    else:
        answer += (int(a) - int(b))
    return answer