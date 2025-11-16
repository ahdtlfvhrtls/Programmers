def solution(my_string, indices):
    answer = ''
    for i, l in enumerate(my_string):
        if i not in indices:
            answer += l
    return answer