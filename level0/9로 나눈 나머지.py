def solution(number):
    answer = 0
    num = 0
    for i in range(len(number)):
        num += int(number[i])
    answer += int(num) % 9
    return answer