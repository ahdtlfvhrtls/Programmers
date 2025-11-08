def solution(code):
    answer = ''
    mode=0
    for idx, val in enumerate(code):
        if mode == 0:
            if val != "1":
                if idx % 2 == 0:
                    answer += val
            else:
                mode = 1
        else:
            if val!= "1" :
                if idx % 2 != 0:
                    answer += val
            else:
                mode = 0
            
    return "EMPTY" if len(answer) == 0 else answer 