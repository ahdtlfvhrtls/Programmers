def solution(my_string, queries):
    for i, k in queries:
        my_string = my_string[:i] + my_string[i:k+1][::-1] + my_string[k+1:]
    return my_string