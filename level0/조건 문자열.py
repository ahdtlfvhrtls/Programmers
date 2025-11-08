def solution(ineq, eq, n, m):
    answer = 0
    condition = ineq + eq

    if condition == '<=':
        if n <= m:
            answer = 1
        else:
            answer = 0
    elif condition == '>=':
        if n >= m:
            answer = 1
        else:
            answer = 0
    elif condition == '<!':
        if  n < m:  
            answer = 1
        else:
            answer = 0
    elif condition == '>!':
        if  n > m:  
            answer = 1
        else:
            answer = 0
    else:
        answer = 0

    return answer