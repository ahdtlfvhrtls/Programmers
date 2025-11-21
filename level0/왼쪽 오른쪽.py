def solution(str_list):
    
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]