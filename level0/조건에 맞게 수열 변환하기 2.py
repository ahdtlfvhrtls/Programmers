def solution(arr):
    x = 0
    while(True):
        arrx = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                arrx.append(i//2)
            elif i < 50 and i % 2 != 0: