def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        num = i[s:s+l]
        if int(num) > int(k):
            answer += [int(num)]
    return answer